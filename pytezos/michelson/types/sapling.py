from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.types.core import IntType
from pytezos.michelson.micheline import MichelineLiteral


class BLS12_381_G1Type(IntType, prim='bls12_381_g1'):

    def __init__(self, value: int):
        super(BLS12_381_G1Type, self).__init__()
        self.value = value

    def __bytes__(self):
        return self.value.to_bytes(48, 'big')

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_G1Type':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, bytes):
            value = int.from_bytes(py_obj, 'big')
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = int.from_bytes(bytes.fromhex(py_obj), 'big')
        else:
            assert False, f'unexpected value {py_obj}'
        return cls(value)


class BLS12_381_G2Type(IntType, prim='bls12_381_g2'):

    def __init__(self, value: int):
        super(BLS12_381_G2Type, self).__init__()
        self.value = value

    def __bytes__(self):
        return self.value.to_bytes(96, 'big')

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_G2Type':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, bytes):
            value = int.from_bytes(py_obj, 'big')
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = int.from_bytes(bytes.fromhex(py_obj), 'big')
        else:
            assert False, f'unexpected value {py_obj}'
        return cls(value)


class BLS12_381_FrType(IntType, prim='bls12_381_fr'):

    def __init__(self, value: int):
        super(BLS12_381_FrType, self).__init__()
        self.value = value

    def __bytes__(self):
        return self.value.to_bytes(96, 'big')

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_FrType':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, bytes):
            value = int.from_bytes(py_obj, 'big')
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = int.from_bytes(bytes.fromhex(py_obj), 'big')
        else:
            assert False, f'unexpected value {py_obj}'
        return cls(value)


class SaplingTransactionType(MichelsonType, prim='sapling_transaction', args_len=1):
    pass


class SaplingStateType(MichelsonType, prim='sapling_state', args_len=1):

    def __repr__(self):
        return ''

    @staticmethod
    def empty(memo_size: int):
        cls = SaplingStateType.create_type(args=[MichelineLiteral.create(memo_size)])
        return cls()
