import atexit
import unittest
from time import sleep
from typing import Optional

import requests.exceptions
from testcontainers.core.generic import DockerContainer  # type: ignore

from pytezos.client import PyTezosClient

# NOTE: Container object is a singleton which will be used in all tests inherited from class _SandboxedNodeTestCase
# and stopped after all tests are completed.
node_container: Optional[DockerContainer] = None
node_container_client: PyTezosClient = PyTezosClient()
node_fitness: int = 1


class SandboxedNodeTestCase(unittest.TestCase):
    IMAGE = 'bakingbad/sandboxed-node:v9.0-rc1-1'
    PROTOCOL = 'PtEdo2Zk'

    def run(self, result: Optional[unittest.TestResult] = None):
        """ Stop after first error """
        # FIXME: not working with pytest, type(result) == _pytest.unittest.TestCaseFunction
        super().run(result)

    def activate(self, protocol_alias: str, reset: bool = False):
        return self.get_client().using(key='dictator') \
            .activate_protocol(protocol_alias) \
            .fill(block_id='genesis' if reset else 'head').sign().inject()

    def bake_block(self):
        return self.get_client().using(key='bootstrap1') \
            .bake_block() \
            .fill().work().sign().inject()

    @property
    def client(self) -> PyTezosClient:
        return self.get_client().using(key='bootstrap2')

    @classmethod
    def get_node_url(cls) -> str:
        container = cls.get_node_container()
        container_id = container.get_wrapped_container().id
        host = container.get_docker_client().bridge_ip(container_id)
        return f'http://{host}:8732'

    @classmethod
    def get_node_container(cls) -> DockerContainer:
        if node_container is None:
            raise RuntimeError('Sandboxed node container is not running')
        return node_container

    @classmethod
    def get_client(cls):
        return node_container_client.using(
            shell=cls.get_node_url(),
        )

    @classmethod
    def _create_node_container(cls) -> DockerContainer:
        return DockerContainer(
            cls.IMAGE,
        )

    @classmethod
    def setUpClass(cls) -> None:
        global node_container
        if not node_container:
            node_container = cls._create_node_container()
            node_container.start()
            cls._wait_for_connection()
            atexit.register(node_container.stop)

    @classmethod
    def _wait_for_connection(cls) -> None:
        client = cls.get_client()
        while True:
            try:
                client.shell.node.get("/version/")
                break
            except requests.exceptions.ConnectionError:
                sleep(0.1)
