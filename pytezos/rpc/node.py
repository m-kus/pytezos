import requests
from simplejson import JSONDecodeError
from hashlib import sha1
from urllib.parse import urlencode
from pprint import pformat


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
    __handlers__ = {}

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

    def __init__(self, uri, network=''):
        self.uri = uri
        self.network = network
        self._cache = dict()
        self._session = requests.Session()

    def __repr__(self):
        res = [
            super(RpcNode, self).__repr__(),
            '\nNode address',
            f'{self.uri} ({self.network})',
            '\nCached urls',
            *list(self._cache.keys())
        ]
        return '\n'.join(res)

    def request(self, method, path, **kwargs) -> requests.Response:
        res = self._session.request(
            method=method,
            url=urljoin(self.uri, path),
            headers={
                'content-type': 'application/json',
                'user-agent': 'PyTezos'
            },
            **kwargs
        )
        if res.status_code != 200:
            raise RpcError.from_response(res) from None

        return res

    def get(self, path, params=None, caching=False, cache_key=None, timeout=None):
        if caching:
            if not cache_key:
                cache_key = path
                if params:
                    cache_key += f'?{urlencode(params)}'
            if cache_key in self._cache:
                return self._cache[cache_key]

        res = self.request('GET', path, params=params, timeout=timeout).json()
        if caching:
            self._cache[cache_key] = res

        return res

    def post(self, path, params=None, json=None, caching=False):
        cache_key = None
        if caching:
            cache_key = sha1((path + str(json)).encode()).hexdigest()
            if cache_key in self._cache:
                return self._cache[cache_key]

        response = self.request('POST', path, params=params, json=json)
        try:
            res = response.json()
        except JSONDecodeError:
            res = response.text

        if caching:
            self._cache[cache_key] = res

        return res

    def delete(self, path, params=None):
        return self.request('DELETE', path, params=params).json()

    def put(self, path, params=None):
        return self.request('PUT', path, params=params).json()


class RpcMultiNode(RpcNode):

    def __init__(self, uri, network):
        super(RpcMultiNode, self).__init__(uri=uri, network=network)
        if not isinstance(uri, list):
            self.uri = [uri]
        self.nodes = list(map(lambda x: RpcNode(x, network), self.uri))
        self._next_i = 0

    def __repr__(self):
        res = [
            super(RpcNode, self).__repr__(),
            f'\nNode addresses ({self.network})',
            *self.uri
        ]
        return '\n'.join(res)

    def request(self, method, path, **kwargs) -> requests.Response:
        assert self._next_i < len(self.nodes)
        res = self.nodes[self._next_i].request(method, path, **kwargs)
        self._next_i = (self._next_i + 1) % len(self.nodes)
        return res
