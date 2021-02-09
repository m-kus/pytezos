from typing import Type, Optional

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.micheline import MichelineSequence, Micheline


class OperationType(MichelsonType, prim='operation'):

    def __init__(self, content: dict):
        super(OperationType, self).__init__()
        self.content = content

    def __repr__(self):
        return ''
        # if content['kind'] == 'transaction':
        #     return {'kind': content['kind'],
        #             'target': content['destination'],
        #             'amount': content['amount'],
        #             'entrypoint': content['parameters']['entrypoint'],
        #             'parameters': micheline_to_michelson(content['parameters']['value'])}
        # elif content['kind'] == 'origination':
        #     res = {'kind': content['kind'],
        #            'target': content['originated_contract'],
        #            'amount': content['balance'],
        #            'storage': micheline_to_michelson(content['script']['storage']),
        #            'code': micheline_to_michelson(content['script']['code'])}
        #     if content.get('delegate'):
        #         res['delegate'] = content['delegate']
        #     return res
        # elif content['kind'] == 'delegation':
        #     return {'kind': content['kind'],
        #             'target': content['delegate']}
        # else:
        #     assert False, content['kind']

    @classmethod
    def origination(cls,
                    source: str,
                    script: Type[MichelineSequence],
                    storage: Optional[MichelsonType] = None,
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
        assert isinstance(py_obj, dict)
        assert 'kind' in py_obj
        return cls(content=py_obj)

    def to_literal(self):
        assert False, 'no literal representation'

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        assert False, 'no micheline representation'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return self.content
