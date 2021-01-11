from typing import cast, List, Type, Optional

from pytezos.types.base import MichelsonType
from pytezos.types.core import BytesType


class BLS12_381_G1Type(BytesType, prim='bls12_381_g1'):

    def __init__(self, value: bytes):
        super(BLS12_381_G1Type, self).__init__()
        self.value = value

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_G1Type':
        if isinstance(py_obj, int):
            value = py_obj.to_bytes(48, 'big')
            return cls(value)
        else:
            res = super(BLS12_381_G1Type, cls).from_python_object(py_obj)
            return cast('BLS12_381_G1Type', res)


class BLS12_381_G2Type(BytesType, prim='bls12_381_g2'):

    def __init__(self, value: bytes):
        super(BLS12_381_G2Type, self).__init__()
        self.value = value

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_G2Type':
        if isinstance(py_obj, int):
            value = py_obj.to_bytes(96, 'big')
            return cls(value)
        else:
            res = super(BLS12_381_G2Type, cls).from_python_object(py_obj)
            return cast('BLS12_381_G2Type', res)


class BLS12_381_FrType(BytesType, prim='bls12_381_fr'):

    def __init__(self, value: bytes):
        super(BLS12_381_FrType, self).__init__()
        self.value = value

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_FrType':
        if isinstance(py_obj, int):
            value = py_obj.to_bytes(96, 'big')
            return cls(value)
        else:
            res = super(BLS12_381_FrType, cls).from_python_object(py_obj)
            return cast('BLS12_381_FrType', res)


class SaplingTransactionType(MichelsonType, prim='sapling_transaction', args_len=1):
    pass


class SaplingStateType(MichelsonType, prim='sapling_state', args_len=1):
    pass
