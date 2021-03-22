from typing import Optional, Type

from pytezos.michelson.micheline import MichelineSequence
from pytezos.michelson.types.base import MichelsonType


class OperationType(MichelsonType, prim='operation'):

    def __init__(self, content: dict, ty: Optional[Type[MichelsonType]] = None):
        super(OperationType, self).__init__()
        self.content = content
        self.ty = ty

    def __repr__(self):
        return self.content['kind']

    def __eq__(self, other):
        if not isinstance(other, OperationType):
            return False
        return self.content == other.content

    @classmethod
    def origination(cls,
                    source: str,
                    script: Type[MichelineSequence],
                    storage: MichelsonType,
                    balance: int = 0,
                    delegate: Optional[str] = None) -> 'OperationType':
        content = {
            'kind': 'origination',
            'source': source,
            'script': {
                'code': script.as_micheline_expr(),
                'storage': storage.to_micheline_value()
            },
            'balance': str(balance)
        }
        if delegate is not None:
            content['delegate'] = delegate
        return cls(content, ty=type(storage))

    @classmethod
    def delegation(cls, source: str, delegate: Optional[str] = None) -> 'OperationType':
        content = {
            'kind': 'delegation',
            'source': source,
            'delegate': delegate
        }
        return cls(content)

    @classmethod
    def transaction(cls, source: str, destination: str, amount: int, entrypoint: str, parameter: MichelsonType) \
            -> 'OperationType':
        content = {
            'kind': 'transaction',
            'source': source,
            'destination': destination,
            'amount': str(amount),
            'parameters': {
                'entrypoint': entrypoint,
                'value': parameter.to_micheline_value()
            }
        }
        return cls(content, ty=type(parameter))

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        kind = self.content['kind']
        assert self.ty, f'data type is not defined for {kind}'
        if kind == 'transaction':
            data = self.ty.from_micheline_value(self.content['parameters']['value'])
        elif kind == 'origination':
            data = self.ty.from_micheline_value(self.content['script']['storage'])
        else:
            assert False, f'not applicable for {kind}'
        return data.to_python_object(try_unpack=try_unpack)
