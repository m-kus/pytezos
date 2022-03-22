import atexit
import logging
import unittest
from concurrent.futures import Future, ThreadPoolExecutor, wait
from threading import Event
from time import sleep
from typing import Optional

import requests.exceptions
from testcontainers.core.generic import DockerContainer  # type: ignore

from pytezos.client import PyTezosClient
from pytezos.operation.group import OperationGroup
from pytezos.sandbox.parameters import LATEST

DOCKER_IMAGE = 'bakingbad/sandboxed-node:v12.0-2'
MAX_ATTEMPTS = 100
ATTEMPT_DELAY = 0.1
TEZOS_NODE_PORT = 8732

# NOTE: Container object is a singleton which will be used in all tests inherited from class _SandboxedNodeTestCase
# and stopped after all tests are completed.
node_container: Optional['SandboxedNodeContainer'] = None
executor: Optional[ThreadPoolExecutor] = None


class SandboxedNodeContainer(DockerContainer):
    def __init__(self, image=DOCKER_IMAGE, port=TEZOS_NODE_PORT):
        super(SandboxedNodeContainer, self).__init__(image, remove=True)
        self.with_bind_ports(TEZOS_NODE_PORT, port)
        self.url = f'http://localhost:{port}'
        self.client = PyTezosClient().using(shell=self.url, key='bootstrap2')

    def start(self):
        super(SandboxedNodeContainer, self).start()
        if self.get_wrapped_container() is None:
            raise RuntimeError('Failed to create a container')

    def wait_for_connection(self, max_attempts=MAX_ATTEMPTS, attempt_delay=ATTEMPT_DELAY) -> bool:
        attempts = max_attempts
        while attempts > 0:
            try:
                self.client.shell.node.get("/version/")
                return True
            except requests.exceptions.ConnectionError:
                sleep(attempt_delay)
                attempts -= 1
        return False

    def activate(self, protocol=LATEST, reset=False):
        return self.client.using(key='dictator').activate_protocol(protocol).fill(block_id='genesis' if reset else 'head').sign().inject()

    def bake(self, key='bootstrap1', min_fee: int = 0):
        return self.client.using(key=key).bake_block(min_fee).fill().work().sign().inject()

    def get_client(self, key='bootstrap2'):
        return self.client.using(key=key)


class SandboxedNodeTestCase(unittest.TestCase):
    """Perform tests with sanboxed node in Docker container."""

    IMAGE: str = DOCKER_IMAGE
    "Docker image to use"

    PORT: int = TEZOS_NODE_PORT
    "Port to expose to host machine"

    PROTOCOL: str = LATEST
    "Hash of protocol to activate"

    @classmethod
    def setUpClass(cls) -> None:
        """Spin up sandboxed node container and activate protocol."""
        global node_container  # pylint: disable=global-statement
        if not node_container:
            node_container = SandboxedNodeContainer(image=cls.IMAGE, port=cls.PORT)
            node_container.start()
            if not node_container.wait_for_connection():
                node_container.stop()
                logging.error('failed to connect to %s', node_container.url)
                return
            atexit.register(node_container.stop)

        node_container.activate(cls.PROTOCOL, reset=True)

    @classmethod
    def _get_node_container(cls) -> SandboxedNodeContainer:
        if node_container is None:
            raise RuntimeError('Sandboxed node container is not running')
        return node_container

    @classmethod
    def activate(cls, protocol_alias: str, reset: bool = False) -> OperationGroup:
        """Activate protocol."""
        return cls._get_node_container().activate(protocol=protocol_alias, reset=reset)

    @classmethod
    def get_client(cls, key='bootstrap2') -> PyTezosClient:
        return cls._get_node_container().get_client(key)

    @classmethod
    def bake_block(cls, min_fee: int = 0, key='bootstrap1') -> OperationGroup:
        """Bake new block.

        :param key: override baker account
        :param min_fee: minimum fee of operation to be included in block
        """
        return cls._get_node_container().bake(key=key, min_fee=min_fee)

    @property
    def client(self) -> PyTezosClient:
        """PyTezos client to interact with sandboxed node."""
        return self._get_node_container().client


class SandboxedNodeAutoBakeTestCase(SandboxedNodeTestCase):
    exit_event: Optional[Event] = None
    baker: Optional[Future] = None

    TIME_BETWEEN_BLOCKS = 3
    BAKER_KEY = 'bootstrap1'

    @staticmethod
    def autobake(time_between_blocks: int, node_url: str, key: str, exit_event: Event):
        logging.info("Baker thread started")
        client = PyTezosClient().using(shell=node_url, key=key)
        ptr = 0
        while not exit_event.is_set():
            if ptr % time_between_blocks == 0:
                client.bake_block().fill().work().sign().inject()
            sleep(1)
            ptr += 1
        logging.info("Baker thread stopped")

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        global executor  # pylint: disable=global-statement
        if not executor:
            executor = ThreadPoolExecutor(1)
        global node_container
        if not node_container:
            raise RuntimeError('sandboxed node container is not created')
        cls.exit_event = Event()  # type: ignore
        cls.baker = executor.submit(cls.autobake, cls.TIME_BETWEEN_BLOCKS, node_container.url, cls.BAKER_KEY, cls.exit_event)

    @classmethod
    def tearDownClass(cls) -> None:
        assert cls.exit_event
        assert cls.baker
        cls.exit_event.set()
        wait([cls.baker])
