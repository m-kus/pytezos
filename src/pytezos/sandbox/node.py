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

DOCKER_IMAGE = 'bakingbad/sandboxed-node:v11.0-1'

# NOTE: Container object is a singleton which will be used in all tests inherited from class _SandboxedNodeTestCase
# and stopped after all tests are completed.
node_container: Optional[DockerContainer] = None
node_container_client: PyTezosClient = PyTezosClient()
node_fitness: int = 1

executor: Optional[ThreadPoolExecutor] = None


class SandboxedNodeTestCase(unittest.TestCase):
    """Perform tests with sanboxed node in Docker container."""

    IMAGE: str = DOCKER_IMAGE
    "Docker image to use"

    PORT: Optional[int] = None
    "Port to expose to host machine"

    PROTOCOL: str = LATEST
    "Hash of protocol to activate"

    @classmethod
    def setUpClass(cls) -> None:
        """Spin up sandboxed node container and activate protocol."""
        global node_container  # pylint: disable=global-statement
        if not node_container:
            node_container = cls._create_node_container()
            node_container.start()
            cls._wait_for_connection()
            atexit.register(node_container.stop)

        cls.activate(cls.PROTOCOL, reset=True)

    @classmethod
    def activate(cls, protocol_alias: str, reset: bool = False) -> OperationGroup:
        """Activate protocol."""
        return (
            cls.get_client()
            .using(key='dictator')
            .activate_protocol(protocol_alias)
            .fill(block_id='genesis' if reset else 'head')
            .sign()
            .inject()
        )

    @classmethod
    def get_node_url(cls) -> str:
        """Get sandboxed node URL."""
        container = cls._get_node_container()
        container_id = container.get_wrapped_container().id
        host = container.get_docker_client().bridge_ip(container_id)
        return f'http://{host}:8732'

    @classmethod
    def _get_node_container(cls) -> DockerContainer:
        if node_container is None:
            raise RuntimeError('Sandboxed node container is not running')
        return node_container

    @classmethod
    def get_client(cls) -> PyTezosClient:
        return node_container_client.using(
            shell=cls.get_node_url(),
        )

    @classmethod
    def _create_node_container(cls) -> DockerContainer:
        container = DockerContainer(
            cls.IMAGE,
        )
        if cls.PORT:
            container.ports[8732] = cls.PORT
        return container

    @classmethod
    def _wait_for_connection(cls) -> None:
        client = cls.get_client()
        while True:
            try:
                client.shell.node.get("/version/")
                break
            except requests.exceptions.ConnectionError:
                sleep(0.1)

    @classmethod
    def bake_block(cls, min_fee: int = 0) -> OperationGroup:
        """Bake new block.

        :param min_fee: minimum fee of operation to be included in block
        """
        return cls.get_client().using(key='bootstrap1').bake_block(min_fee).fill().work().sign().inject()

    @property
    def client(self) -> PyTezosClient:
        """PyTezos client to interact with sandboxed node."""
        return self.get_client().using(key='bootstrap2')


class SandboxedNodeAutoBakeTestCase(SandboxedNodeTestCase):
    exit_event: Optional[Event] = None
    baker: Optional[Future] = None

    TIME_BETWEEN_BLOCKS = 3

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
        cls.exit_event = Event()  # type: ignore
        cls.baker = executor.submit(cls.autobake, cls.TIME_BETWEEN_BLOCKS, cls.get_node_url(), 'bootstrap1', cls.exit_event)

    @classmethod
    def tearDownClass(cls) -> None:
        assert cls.exit_event
        assert cls.baker
        cls.exit_event.set()
        wait([cls.baker])
