import json
from pprint import pformat

import requests
from simplejson import JSONDecodeError

from pytezos.logging import logger


def urljoin(*args):
    return "/".join(map(lambda x: str(x).strip('/'), args))


def gen_error_variants(error_id) -> list:
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
    def __init_subclass__(cls, error_id=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if isinstance(error_id, list):
            for eid in error_id:
                cls.__handlers__[eid] = cls
        else:
            assert error_id is not None
            cls.__handlers__[error_id] = cls

    @classmethod
    def from_errors(cls, errors: list):
        if not errors:
            return RpcError('Unspecified error')

        # FIXME: Only first error is being processed
        error = errors[-1]
        for key in gen_error_variants(error['id']):
            if key in cls.__handlers__:
                handler = cls.__handlers__[key]
                return handler(error)
        return RpcError(error)

    @classmethod
    def from_response(cls, res: requests.Response):
        if res.headers.get('content-type') == 'application/json':
            errors = res.json()
            assert isinstance(errors, list)
            return cls.from_errors(errors)
        else:
            return RpcError(res.text)

    def __str__(self):
        return pformat(self.args)


class RpcNode:

    def __init__(self, uri):
        self.uri = uri
        self._session = requests.Session()

    def __repr__(self):
        res = [
            super(RpcNode, self).__repr__(),
            '\nNode address',
            self.uri
        ]
        return '\n'.join(res)

    def request(self, method, path, **kwargs) -> requests.Response:
        logger.debug('>>>>> %s %s\n%s', method, path, json.dumps(kwargs, indent=4))
        res = self._session.request(
            method=method,
            url=urljoin(self.uri, path),
            headers={
                'content-type': 'application/json',
                'user-agent': 'PyTezos'
            },
            **kwargs
        )
        if res.status_code == 404:
            logger.debug('<<<<< %s\n%s', res.status_code, res.text)
            raise RpcError(f'Not found: {path}')
        elif res.status_code != 200:
            logger.debug('<<<<< %s\n%s', res.status_code, pformat(res.text, indent=4))
            raise RpcError.from_response(res)

        logger.debug('<<<<< %s\n%s', res.status_code, json.dumps(res.json(), indent=4))
        return res

    def get(self, path, params=None, timeout=None):
        return self.request('GET', path, params=params, timeout=timeout).json()

    def post(self, path, params=None, json=None):
        response = self.request('POST', path, params=params, json=json)
        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    def delete(self, path, params=None):
        return self.request('DELETE', path, params=params).json()

    def put(self, path, params=None):
        return self.request('PUT', path, params=params).json()


class RpcMultiNode(RpcNode):

    def __init__(self, uri):
        super(RpcMultiNode, self).__init__(uri=uri)
        if not isinstance(uri, list):
            self.uri = [uri]
        self.nodes = list(map(lambda x: RpcNode(x), self.uri))
        self._next_i = 0

    def __repr__(self):
        res = [
            super(RpcNode, self).__repr__(),
            f'\nNode addresses',
            *self.uri
        ]
        return '\n'.join(res)

    def request(self, method, path, **kwargs) -> requests.Response:
        assert self._next_i < len(self.nodes)
        res = self.nodes[self._next_i].request(method, path, **kwargs)
        self._next_i = (self._next_i + 1) % len(self.nodes)
        return res
