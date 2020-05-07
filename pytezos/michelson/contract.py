from functools import lru_cache
from collections import defaultdict
from os.path import basename, exists, expanduser, dirname, join

from pytezos.tools.docstring import get_class_docstring, InlineDocstring
from pytezos.michelson.docstring import generate_docstring
from pytezos.michelson.micheline import make_default, michelson_to_micheline, is_optional
from pytezos.michelson.formatter import micheline_to_michelson
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, build_big_map_schema
from pytezos.michelson.pack import get_key_hash


class ContractParameter(metaclass=InlineDocstring):

    def __init__(self, section):
        self.code = section
        self.schema = build_schema(section)
        self.__doc__ = generate_docstring(self.schema, 'parameter')

    def __repr__(self):
        res = [
            super(ContractParameter, self).__repr__(),
            f'\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def _get_entry_root(self, entrypoint):
        if entrypoint in {'default', 'root'}:
            return '0'
        else:
            bin_path = self.schema.json_to_bin[f'/{entrypoint}']
            if is_optional(self.schema, bin_path):
                bin_path = bin_path[:-1]
            return bin_path

    def decode(self, data):
        """
        Convert Micheline data into Python object using internal schema.
        :param data: Micheline expression or Michelson string or {entrypoint: "string", value: "expression"}
        :return: object
        """
        if isinstance(data, dict) and set(data.keys()) == {'entrypoint', 'value'}:
            if data['entrypoint'] not in {'root', 'default'}:
                res = decode_micheline(val_expr=data['value'],
                                       type_expr=self.code,
                                       schema=self.schema,
                                       root=self._get_entry_root(data['entrypoint']))
                return {data['entrypoint']: res}
            else:
                return decode_micheline(val_expr=data['value'],
                                        type_expr=self.code,
                                        schema=self.schema)  # TODO: default subpath (see BCD issue)
        else:
            if isinstance(data, str):
                data = michelson_to_micheline(data)

            return decode_micheline(val_expr=data, type_expr=self.code, schema=self.schema)

    def encode(self, data, entrypoint=None):
        """
        Convert Python object to Micheline expression using internal schema.
        :param data: Python object
        :param entrypoint: Force entrypoint
        :return: object
        """
        if entrypoint is None:
            if isinstance(data, dict) and len(data) == 1:
                entrypoint = next(iter(data))
                if not any(map(lambda x: x.get('fieldname') == entrypoint, self.schema.metadata.values())):
                    entrypoint = 'default'  # prevent auto-generated entrypoint names, like `entrypoint_1`
            else:
                entrypoint = 'default'

            if entrypoint == 'default':
                value = encode_micheline(data, self.schema)
            else:
                value = encode_micheline(data[entrypoint], self.schema, root=self._get_entry_root(entrypoint))
        else:
            value = encode_micheline(data, self.schema, root=self._get_entry_root(entrypoint))

        return dict(entrypoint=entrypoint, value=value)

    def entries(self, default='call'):
        """
        Get list of entrypoints: names and docstrings.
        :param default: Name of the single entrypoint
        :return: list[tuple]
        """
        if self.schema.metadata['0']['prim'] == 'or':
            entries = [
                (self.schema.bin_names[bin_path], bin_path)
                for bin_path in self.schema.metadata['0']['args']
            ]
        else:
            entries = [(default, '0')]

        def make_docs(bin_path):
            if self.schema.bin_types[bin_path] in ['namedtuple', 'router']:
                title = 'kwargs'
            else:
                title = 'args'
            return generate_docstring(self.schema, title, bin_path)

        return list(map(lambda x: (x[0], make_docs(x[1])), entries))


class ContractStorage(metaclass=InlineDocstring):

    def __init__(self, section):
        self.code = section
        self.schema = build_schema(section)
        self.big_map_schema = None
        self.__doc__ = generate_docstring(self.schema, 'storage')

    def __repr__(self):
        res = [
            super(ContractStorage, self).__repr__(),
            f'\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def decode(self, data):
        """
        Convert Micheline data into Python object using internal schema.
        :param data: Micheline expression or Michelson string
        :return: object
        """
        if isinstance(data, str):
            data = michelson_to_micheline(data)
        return decode_micheline(val_expr=data,
                                type_expr=self.code,
                                schema=self.schema)

    def encode(self, data):
        """
        Convert Python object to Micheline expression using internal schema.
        :param data: Python object
        :return: object
        """
        return encode_micheline(data, self.schema)

    def default(self, root='0'):
        """
        Try to generate empty storage, returns Micheline expression
        :param root: binary path to start from, default is '0'
        :return: object
        """
        return make_default(self.schema.bin_types, root)

    def big_map_init(self, data):
        """
        Initialize big_map_id <-> JSON path mapping (since Babylon)
        :param data: Micheline expression (raw contract storage)
        """
        self.big_map_schema = build_big_map_schema(data, self.schema)

    def _locate_big_map(self, big_map_id=None):
        def get_json_path(bp):
            return next((k.lstrip('/') for k, v in self.schema.json_to_bin.items() if v == bp),
                        self.schema.bin_names.get(bp))

        if big_map_id is None:
            # Default Big Map location (prior to Babylon https://blog.nomadic-labs.com/michelson-updates-in-005.html)
            return '000', '001', get_json_path('00')
        else:
            assert self.big_map_schema, "Please call `big_map_init` first"
            bin_path = self.big_map_schema.id_to_bin[int(big_map_id)]
            return bin_path + '0', bin_path + '1', get_json_path(bin_path)

    def big_map_id(self, big_map_path) -> int:
        assert self.big_map_schema, "Please call `big_map_init` first"
        bin_path = self.schema.json_to_bin[big_map_path]
        return self.big_map_schema.bin_to_id[bin_path]

    def _is_old_style_big_map(self) -> bool:
        return len(self.big_map_schema.bin_to_id) == 1 \
               and next(iter(self.big_map_schema.bin_to_id)) == '00'

    def big_map_query(self, path):
        """
        Construct a query for big_map_get request
        :param path: BigMap key, string, int, or hex-string
        (since Babylon you can have more than one BigMap at arbitrary position)
        :return: dict
        """
        key = basename(path)
        big_map_path = dirname(path)
        big_map_id = self.big_map_id(join('/', big_map_path)) if big_map_path else None
        key_root, _, _ = self._locate_big_map(big_map_id)
        encoded_key = encode_micheline(data=key, schema=self.schema, root=key_root)
        key_hash = get_key_hash(encoded_key, self.code, bin_path=key_root)

        if big_map_id:
            query = dict(
                big_map_id=big_map_id,
                script_expr=key_hash)
        else:
            query = dict(
                key=encoded_key,
                type={'prim': self.schema.metadata[key_root]['prim']})

        return query

    def big_map_decode(self, value, big_map_id=None):
        """
        Convert big_map_get result into a Python object
        :param value: Micheline expression for a BigMap entry
        (since Babylon you can have more than one BigMap at arbitrary position)
        :param big_map_id: BigMap pointer (integer)
        :return: object
        """
        _, value_root, _ = self._locate_big_map(big_map_id)
        return decode_micheline(val_expr=value,
                                type_expr=self.code,
                                schema=self.schema,
                                root=value_root)

    def big_map_diff_decode(self, diff: list) -> dict:
        """
        Convert big_map_diff from operation_result section into Python objects
        :param diff: [{"key": $micheline, "value": $micheline}, ...]
        :return: {"path/to/big/map": {"key": "value"}} for Babylon; {"key": "value"} for old contracts
        """
        if not isinstance(diff, list):
            return {}

        res = defaultdict(dict)

        for item in diff:
            if item.get('action') == 'alloc':
                continue

            big_map_id = item.get('big_map')
            key_root, value_root, json_path = self._locate_big_map(big_map_id)

            key = decode_micheline(val_expr=item['key'],
                                   type_expr=self.code,
                                   schema=self.schema,
                                   root=key_root)
            if item.get('value'):
                value = decode_micheline(val_expr=item['value'],
                                         type_expr=self.code,
                                         schema=self.schema,
                                         root=value_root)
            else:
                value = None

            if big_map_id and not self._is_old_style_big_map() and json_path:
                res[json_path][key] = value
            else:
                res[key] = value  # Backward compatibility

        return dict(res)

    # DEPRECATED (For old contracts only)
    def big_map_diff_encode(self, big_map: dict):
        """
        Convert Python representation of BigMap (dict) into big_map_diff
        :param big_map: { $key: $micheline, ... }
        :return: [{"key": $micheline, "value": $micheline}, ... ]
        """
        key_root, value_root, _ = self._locate_big_map()

        def make_item(x):
            key = encode_micheline(data=x[0],
                                   schema=self.schema,
                                   root=key_root,
                                   binary=True)
            if x[1] is not None:
                value = encode_micheline(data=x[1],
                                         schema=self.schema,
                                         root=value_root,
                                         binary=True)
            else:
                value = None
            return {"key": key, "value": value}

        return list(map(make_item, big_map.items()))


class Contract(metaclass=InlineDocstring):

    def __init__(self, code: list):
        self.code = code

    def __repr__(self):
        res = [
            super(Contract, self).__repr__(),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def __str__(self):
        return self.text

    @property
    @lru_cache(maxsize=None)
    def parameter(self) -> ContractParameter:
        return ContractParameter(next(s for s in self.code if s['prim'] == 'parameter'))

    @property
    @lru_cache(maxsize=None)
    def storage(self) -> ContractStorage:
        return ContractStorage(next(s for s in self.code if s['prim'] == 'storage'))

    @property
    @lru_cache(maxsize=None)
    def text(self):
        return micheline_to_michelson(self.code)

    @classmethod
    def from_micheline(cls, code):
        """
        Create contract from micheline expression.
        :param code: [{'prim': 'parameter'}, {'prim': 'storage'}, {'prim': 'code'}]
        :return: Contract
        """
        return cls(code)

    @classmethod
    def from_michelson(cls, text):
        """
        Create contract from michelson source code.
        :param text:
        :return: Contract
        """
        return cls(michelson_to_micheline(text))

    @classmethod
    def from_file(cls, path):
        """
        Create contract from michelson source code stored in file.
        :param path: Path to the `.tz` file
        :return: Contract
        """
        with open(expanduser(path)) as f:
            return cls.from_michelson(f.read())

    def save_file(self, path, overwrite=False):
        """
        Save Michelson code to file
        :param path: Output path
        :param overwrite: Default is False
        """
        path = expanduser(path)
        if exists(path) and not overwrite:
            raise FileExistsError(path)

        with open(path, 'w+') as f:
            f.write(self.text)

    def script(self, storage=None, original=True):
        """
        Generate script for contract origination
        :param storage: Python object, leave None to generate empty
        :param original: Keep the original code (initialized), which is default.
        Otherwise factory-specific changes may applied, e.g. different annotations
        :return: {"code": $Micheline, "storage": $Micheline}
        """
        if storage is None:
            storage = self.storage.default()
        else:
            storage = self.storage.encode(storage)

        if original:
            code = self.code
        else:
            code = [
                self.parameter.code,
                self.storage.code,
                self.code[-1]
            ]

        return {
            "code": code,
            "storage": storage
        }
