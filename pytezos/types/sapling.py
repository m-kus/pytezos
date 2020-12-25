from pytezos.types.base import MichelsonType


class BLS12_381_FrType(MichelsonType, prim='bls12_381_fr'):

    @staticmethod
    def to_bytes(value: int) -> bytes:
        return value.to_bytes(48, 'big')

    def assert_value_defined(self):
        assert isinstance(self.value, int) or isinstance(self.value, bytes), \
            f'expected int or bytes, got {type(self.value).__name__}'

    def parse_micheline_value(self, val_expr) -> 'MichelsonType':
        if isinstance(val_expr, str):
            pass

    def parse_python_object(self, py_obj) -> 'MichelsonType':
        if isinstance(py_obj, bytes):
            value = py_obj
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = bytes.fromhex(py_obj)
        elif isinstance(py_obj, int):
            value = self.to_bytes(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return self.spawn(value)


class BLS12_381_G1Type(MichelsonType, prim='bls12_381_g1'):
    pass


class BLS12_381_G2Type(MichelsonType, prim='bls12_381_g2'):
    pass


class SaplingStateType(MichelsonType, prim='sapling_state'):
    pass


class SaplingTransactionType(MichelsonType, prim='sapling_transaction'):
    pass