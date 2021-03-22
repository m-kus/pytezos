import json
import re
from contextlib import suppress
from os.path import dirname, join
from typing import Any, Callable, Dict, List, Optional, Union, cast

import requests  # type: ignore
from attr import dataclass
from bravado.client import SwaggerClient
from cattrs_extras.converter import Converter
from jsonschema import validate as jsonschema_validate  # type: ignore


def to_camelcase(string: str) -> str:
    expression = re.compile("[^A-Za-z]+")
    words = expression.split(string)
    if len(words) == 1:
        string = string[0].lower() + string[1:]
        return string
    return ''.join(w.lower() if i == 0 else w.title() for i, w in enumerate(words))

metadata_json_replace_table = {
    '"return-type":': '"returnType":',
    '"michelson-storage-view":': '"michelsonStorageView":',
}

with open(join(dirname(__file__), 'metadata-schema.json')) as file:
    metadata_schema = json.load(file)


@dataclass(kw_only=True, frozen=True)
class StaticError:
    error: str
    expansion: str
    languages: Optional[List[str]] = None


@dataclass(kw_only=True, frozen=True)
class DynamicError:
    view: str
    languages: Optional[List[str]] = None


@dataclass(kw_only=True, frozen=True)
class License:
    name: str
    details: Optional[str] = None


@dataclass(kw_only=True, frozen=True)
class RestApiView:
    specificationUri: str
    baseUri: Optional[str] = None
    path: str
    method: Optional[str] = None

    def as_swagger_entrypoint(self):
        entrypoint = SwaggerClient.from_url(self.specificationUri)
        for subpath in self.path.strip('/').split('/'):
            entrypoint = getattr(entrypoint, subpath)

        def call(*args, **kwargs):
            response = entrypoint(*args, **kwargs)
            return response.response().result

        return call


@dataclass(kw_only=True, frozen=True)
class RestApiViewImplementation:
    restApiQuery: RestApiView


@dataclass(kw_only=True, frozen=True)
class MichelsonStorageView:
    parameter: Optional[Dict[str, Any]] = None
    returnType: Dict[str, Any]
    code: List[Dict[str, Any]]
    annotations: Optional[List[Dict[str, Any]]] = None
    version: Optional[str] = None

    def as_contract(self, storage_type_expr: Dict[str, Any]):
        from pytezos.contract.interface import ContractInterface

        view_type = self.parameter or {'prim': 'unit'}
        contract = ContractInterface.from_micheline([
            {'prim': 'parameter', 'args': [{'prim': 'pair', 'args': [view_type, storage_type_expr]}]},
            {'prim': 'storage', 'args': [{'prim': 'option', 'args': [self.returnType]}]},
            {'prim': 'code', 'args': [[
                {'prim': 'CAR'},
                self.code,
                {'prim': 'SOME'},
                {'prim': 'NIL', 'args': [{'prim': 'operation'}]},
                {'prim': 'PAIR'}
            ]]},
        ])
        return contract


@dataclass(kw_only=True, frozen=True)
class MichelsonStorageViewImplementation:
    michelsonStorageView: MichelsonStorageView


@dataclass(kw_only=True, frozen=True)
class View:
    name: str
    description: Optional[str] = None
    implementations: List[Union[MichelsonStorageViewImplementation, RestApiViewImplementation]]
    pure: bool = False

    def get_entrypoint(self, storage_type_expr) -> Callable:
        if len(self.implementations) != 1:
            raise Exception
        imp = self.implementations[0]
        if isinstance(imp, MichelsonStorageViewImplementation):
            return imp.michelsonStorageView.as_contract(storage_type_expr).default
        elif isinstance(imp, RestApiViewImplementation):
            return imp.restApiQuery.as_swagger_entrypoint()
        raise NotImplementedError('Unknown view implementation')


@dataclass(kw_only=True)
class ContractMetadata:
    name: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None
    license: Optional[License] = None
    authors: Optional[List[str]] = None
    interfaces: Optional[List[str]] = None
    errors: Optional[List[Union[StaticError, DynamicError]]] = None
    views: Optional[List[View]] = None

    def __attrs_post_init__(self):
        self._storage_type_expr = None

    def __getattribute__(self, name: str) -> Callable:
        with suppress(AttributeError):
            return super().__getattribute__(name)
        try:
            view = self.views_by_name[name]
            return view.get_entrypoint(self._storage_type_expr)
        except KeyError as e:
            raise KeyError(f'Unknown view `{name}`, available: {list(self.views_by_name.keys())}') from e

    def set_storage_type_expr(self, val):
        self._storage_type_expr = val

    @property
    def views_by_name(self):
        return {to_camelcase(v.name): v for v in self.views}

    # FIXME: Unnecessary multiple JSON conversions
    @classmethod
    def fix_metadata_json(cls, metadata_json: Dict[str, Any]) -> Dict[str, Any]:
        metadata_json_string = json.dumps(metadata_json)
        for from_, to in metadata_json_replace_table.items():
            metadata_json_string = metadata_json_string.replace(from_, to)
        return json.loads(metadata_json_string)

    @classmethod
    def validate_metadata_json(cls, metadata_json: Dict[str, Any]) -> None:
        jsonschema_validate(instance=metadata_json, schema=metadata_schema)

    @classmethod
    def from_file(cls, path: str) -> 'ContractMetadata':
        with open(path) as file:
            metadata_json = json.load(file)
            return cls.from_json(metadata_json)

    @classmethod
    def from_json(cls, metadata_json: Dict[str, Any]) -> 'ContractMetadata':
        metadata_json = cls.fix_metadata_json(metadata_json)
        cls.validate_metadata_json(metadata_json)
        return Converter().structure(metadata_json, ContractMetadata)

    @classmethod
    def from_storage(cls, storage, path: str) -> 'ContractMetadata':  # FIXME: accept tezos-storage URI
        metadata_storage = storage['metadata'][path].data
        metadata_json = json.loads(cast(bytes, metadata_storage.to_literal().literal))
        return cls.from_json(metadata_json)

    @classmethod
    def from_url(cls, url: str) -> 'ContractMetadata':  # pylint: disable=no-self-use
        metadata_json = requests.get(url).json()
        return cls.from_json(metadata_json)

    @classmethod
    def from_ipfs(cls, hash_: str) -> 'ContractMetadata':  # pylint: disable=no-self-use
        metadata_json = requests.get(f'https://ipfs.io/ipfs/{hash_}').json()
        return cls.from_json(metadata_json)
