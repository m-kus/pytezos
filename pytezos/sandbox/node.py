import atexit
import unittest
from datetime import datetime
from time import sleep, time
from typing import Any, Dict, Optional

import requests.exceptions
from testcontainers.core.generic import DockerContainer  # type: ignore

from pytezos import logger
from pytezos.block.header import BlockHeader
from pytezos.client import PyTezosClient

# NOTE: Container object is a singleton which will be used in all tests inherited from class _SandboxedNodeTestCase and stopped after
# NOTE: all tests are completed.
node_container: Optional[DockerContainer] = None
node_container_client: PyTezosClient = PyTezosClient()


class SandboxedNodeTestCase(unittest.TestCase):
    IMAGE = 'bakingbad/sandboxed-node:v8.2-2'

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

    def get_current_protocol(self) -> Dict[str, Any]:
        return self.get_client().shell.block.protocols()
