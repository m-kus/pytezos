from os.path import dirname

from pytezos.jupyter import InlineDocstring, get_attr_docstring, get_class_docstring
from pytezos.rpc.docs import rpc_docs
from pytezos.rpc.node import RpcNode


def format_docstring(class_type, query_path):
    res = ['']
    methods = {
        'GET': '()',
        'POST': '.post()',
        'PUT': '.put()',
        'DELETE': '.delete()'
    }
    rpc_doc = rpc_docs.get(query_path, {})

    for method, func in methods.items():
        if method in rpc_doc:
            docstring = get_attr_docstring(class_type, method.lower())
            if not docstring:
                docstring = f'\n{rpc_doc[method]["descr"]}\n'
                for arg in rpc_doc[method]['args']:
                    docstring += f':param {arg["name"]}: {arg["descr"]}\n'
                docstring += f':returns: {rpc_doc[method]["ret"]}\n'

            res.append(f'{func}{docstring}')

    if 'item' in rpc_doc:
        docstring = get_attr_docstring(class_type, '__getitem__')
        if not docstring:
            item = rpc_doc["item"]
            docstring = f'\n:param {item["name"]}: {item["descr"]}\n:returns: Child element\n'

        res.append(f'[]{docstring}')

    if 'props' in rpc_doc:
        properties = rpc_doc['props']
        docstring = '\n'.join(map(lambda x: f'.{x}', properties))
        res.append(f'RPC endpoints\n{docstring}\n')
    else:
        properties = list()

    helpers = get_class_docstring(
        class_type=class_type,
        attr_filter=lambda x: not x.startswith('_')
                              and x not in properties
                              and x.upper() not in methods
                              and x != 'path'
    )
    if helpers:
        res.append(f'Helpers\n{helpers}')

    return '\n'.join(res)


class RpcQuery(metaclass=InlineDocstring):
    __extensions__ = dict()  # type: ignore

    @classmethod
    def __init_subclass__(cls, path: str = '', **kwargs):
        super().__init_subclass__(**kwargs)  # type: ignore
        if isinstance(path, list):
            for sub_path in path:
                cls.__extensions__[sub_path] = cls
        else:
            cls.__extensions__[path] = cls

    def __init__(self, node: RpcNode, path: str = '', params=None, timeout=None):
        self.node = node
        self._wild_path = path
        self._timeout = timeout
        self._params = params or list()
        self.__doc__ = format_docstring(self.__class__, self._wild_path or '/')

    def __repr__(self):
        res = [
            super(RpcQuery, self).__repr__(),
            '\nProperties',
            f'.path\t{self.path or "/"}',
            f'.node\t{self.node.uri}',
            self.__doc__
        ]
        return '\n'.join(res)

    def _spawn_query(self, wild_path, params):
        child_class = self.__extensions__.get(wild_path, RpcQuery)
        return child_class(
            path=wild_path,
            node=self.node,
            params=params
        )

    @property
    def path(self):
        return self._wild_path.format(*self._params)

    def __call__(self, **params):
        return self.node.get(
            path=self.path,
            params=params
        )

    def _getitem(self, item):
        return self._spawn_query(
            wild_path=self._wild_path + '/{}',
            params=self._params + [item]
        )

    def __getattr__(self, attr):
        if not attr.startswith('_'):
            if attr in {'main', 'test', 'head', 'genesis'}:
                return self._getitem(attr)
            else:
                return self._spawn_query(
                    wild_path=f'{self._wild_path}/{attr}',
                    params=self._params
                )
        raise AttributeError(attr)

    def __getitem__(self, child_id):
        return self._getitem(child_id)

    def _get(self, params=None):
        return self.node.get(
            path=self.path,
            params=params,
            timeout=self._timeout
        )

    def _post(self, json=None, params=None):
        return self.node.post(
            path=self.path,
            params=params,
            json=json
        )

    def _put(self, params=None):
        return self.node.put(
            path=self.path,
            params=params
        )

    def _delete(self, params=None):
        return self.node.delete(
            path=self.path,
            params=params
        )

    @property
    def _parent(self):
        dir_path = dirname(self._wild_path)
        return self._spawn_query(
            wild_path=dir_path,
            params=self._params[:dir_path.count('{}')]
        )
