import json
from os.path import dirname, join
from typing import Any, Dict, List, Optional, Union, cast

from attr import dataclass
from cattrs_extras.converter import Converter
from jsonschema import validate as jsonschema_validate
import requests  # type: ignore

from pytezos.context.impl import ExecutionContext

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

    def as_contract(self, storage: Dict[str, Any]):
        from pytezos.contract.interface import ContractInterface

        contract = ContractInterface.from_micheline([
            {'prim': 'parameter', 'args': [self.parameter]},
            {'prim': 'storage', 'args': [storage]},
            {'prim': 'code', 'args': [self.code]},
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

    def as_contract(self, storage):
        if len(self.implementations) != 1:
            raise Exception
        imp = self.implementations[0]
        if isinstance(imp, MichelsonStorageViewImplementation):
            return imp.michelsonStorageView.as_contract(storage)
        elif isinstance(imp, RestApiViewImplementation):
            raise NotImplementedError
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

    def call_view(self, name, storage):
        return self.views_by_name[name].as_contract(storage).default

    @property
    def views_by_name(self):
        return {v.name: v for v in self.views}

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
    def from_json(cls, metadata_json: Dict[str, Any]) -> 'ContractMetadata':
        metadata_json = cls.fix_metadata_json(metadata_json)
        cls.validate_metadata_json(metadata_json)

        return Converter().structure(metadata_json, ContractMetadata)

    @classmethod
    def from_storage(cls, storage, path: str) -> 'ContractMetadata':
        parts = path.split('/')
        if len(parts) == 1:
            # NOTE: KT1JBThDEqyqrEHimhxoUBCSnsKAqFcuHMkP
            metadata_storage = storage['metadata'][parts[0]].data
            metadata_json = json.loads(cast(bytes, metadata_storage.to_literal().literal))
            return cls.from_json(metadata_json)
        elif len(parts) == 2:
            raise NotImplementedError
        raise NotImplementedError('Unknown path format')

    @classmethod
    def from_url(cls, url: str) -> 'ContractMetadata':  # pylint: disable=no-self-use
        metadata_json = requests.get(url).json()
        return cls.from_json(metadata_json)

    @classmethod
    def from_ipfs(cls, hash_: str) -> 'ContractMetadata':  # pylint: disable=no-self-use
        metadata_json = requests.get(f'https://ipfs.io/ipfs/{hash_}').json()
        return cls.from_json(metadata_json)
