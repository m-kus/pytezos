from typing import Type, Optional

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.interpreter.program import MichelsonProgram


class OperationType(MichelsonType, prim='operation'):

    def __init__(self, content: dict):
        super(OperationType, self).__init__()
        self.content = content

    def __repr__(self):
        return self.content.get('kind')

    @classmethod
    def origination(cls,
                    source: str,
                    program: Type[MichelsonProgram],
                    storage: Optional[MichelsonType] = None,
                    balance: int = 0,
                    delegate: Optional[str] = None) -> 'OperationType':
        content = {
            'kind': 'origination',
            'source': source,
            'script': {
                'code': program.as_micheline_expr(),
                'storage': storage.to_micheline_value()
            },
            'balance': str(balance)
        }
        if delegate is not None:
            content['delegate'] = delegate
        return cls(content)

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
        return cls(content)

    @classmethod
    def from_micheline_value(cls, val_expr):
        assert False, 'forbidden'

    @classmethod
    def from_python_object(cls, py_obj) -> 'OperationType':
        pass

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        assert False, 'forbidden'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        pass
