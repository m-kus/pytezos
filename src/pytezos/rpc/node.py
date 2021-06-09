import json
from pprint import pformat
from typing import Any, Dict, List, Optional, Union

import requests
import requests.exceptions
from simplejson import JSONDecodeError

from pytezos.logging import logger


def _urljoin(*args: str) -> str:
    return "/".join(map(lambda x: str(x).strip('/'), args))


def _gen_error_variants(error_id: str) -> List[str]:
    chunks = error_id.split('.')
    variants = [error_id]
    if len(chunks) > 1:
        variants.append(chunks[-2])
        if len(chunks) > 2:
            variants.append('.'.join(chunks[2:]))
    return variants


class RpcError(Exception):
    __handlers__ = {}  # type: ignore

    @classmethod
    def __init_subclass__(cls, error_id: Union[str, List[str]]) -> None:
        super().__init_subclass__()
        if isinstance(error_id, list):
            for eid in error_id:
                cls.__handlers__[eid] = cls
        else:
            cls.__handlers__[error_id] = cls

    @classmethod
    def from_errors(cls, errors: List[Dict[str, Any]]) -> 'RpcError':
        """Create RpcError from "errors" section of response JSON."""
        if not errors:
            return RpcError('Unspecified error')

        # FIXME: Only first error is being processed
        error = errors[-1]
        for key in _gen_error_variants(error['id']):
            if key in cls.__handlers__:
                handler = cls.__handlers__[key]
                return handler(error)
        return RpcError(error)

    @classmethod
    def from_response(cls, res: requests.Response) -> 'RpcError':
        """Create RpcError from requests Response."""
        if res.headers.get('content-type') == 'application/json':
            errors = res.json()
            assert isinstance(errors, list)
            return cls.from_errors(errors)
        else:
            return RpcError(res.text)

    def __str__(self) -> str:
        return pformat(self.args)


class RpcNode:
    """Request proxy for a single Tezos node."""

    def __init__(self, uri: Union[str, List[str]]) -> None:
        if not uri:
            raise RuntimeError()
        if not isinstance(uri, list):
            uri = [uri]
        self.uri = uri

    def __repr__(self) -> str:
        res = [
            super(RpcNode, self).__repr__(),
            '\nNode address',
            self.uri[0],
        ]
        return '\n'.join(res)

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Perform HTTP request to node.

        :param method: one of GET/POST/PUT/DELETE
        :param path: path to endpoint
        :param kwargs: requests.request arguments
        :raises RpcError: node has returned an error
        :returns: node response
        """
        logger.debug('>>>>> %s %s\n%s', method, path, json.dumps(kwargs, indent=4))
        res = requests.request(
            method=method,
            url=_urljoin(self.uri[0], path),
            headers={
                'content-type': 'application/json',
                'user-agent': 'PyTezos',
            },
            **kwargs,
        )
        if res.status_code == 404:
            logger.debug('<<<<< %s\n%s', res.status_code, res.text)
            raise RpcError(f'Not found: {path}')
        if res.status_code != 200:
            logger.debug('<<<<< %s\n%s', res.status_code, pformat(res.text, indent=4))
            raise RpcError.from_response(res)

        logger.debug('<<<<< %s\n%s', res.status_code, json.dumps(res.json(), indent=4))
        return res

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, timeout: Optional[int] = None) -> requests.Response:
        return self.request('GET', path, params=params, timeout=timeout).json()

    def post(self, path: str, params: Optional[Dict[str, Any]] = None, json=None) -> Union[requests.Response, str]:
        response = self.request('POST', path, params=params, json=json)
        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        return self.request('DELETE', path, params=params).json()

    def put(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        return self.request('PUT', path, params=params).json()


class RpcMultiNode(RpcNode):
    """Request proxy for multiple nodes chosen for each request in round-robin order."""

    def __init__(self, uri: Union[str, List[str]]) -> None:
        super().__init__(uri)
        self.nodes = list(map(RpcNode, self.uri))
        self._next_i = 0

    def __repr__(self) -> str:
        res = [
            super().__repr__(),
            '\nNode addresses',
            *self.uri,
        ]
        return '\n'.join(res)

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        assert self._next_i < len(self.nodes)
        res = self.nodes[self._next_i].request(method, path, **kwargs)
        self._next_i = (self._next_i + 1) % len(self.nodes)
        return res
