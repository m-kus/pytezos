from typing import cast

from py_ecc import optimized_bls12_381 as bls12_381
from py_ecc.bls.constants import POW_2_382
from py_ecc.bls.typing import G1Uncompressed, G2Uncompressed
from py_ecc.fields import optimized_bls12_381_FQ as FQ
from py_ecc.fields import optimized_bls12_381_FQ2 as FQ2

from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.types.core import BytesType, IntType


class BLS12_381_FrType(IntType, prim='bls12_381_fr'):
    modulus = 0x73EDA753299D7D483339D80809A1D80553BDA402FFFE5BFEFFFFFFFF00000001

    def __init__(self, value: int):
        super(BLS12_381_FrType, self).__init__()
        self.value = value

    @staticmethod
    def bytes_to_int(value: bytes) -> int:
        assert len(value) <= 32, f'expected no more than 32 bytes, got {len(value)}'
        return int.from_bytes(value, 'little')

    @classmethod
    def from_value(cls, value: int) -> 'BLS12_381_FrType':
        return cls(value % cls.modulus)

    @classmethod
    def from_python_object(cls, py_obj) -> 'BLS12_381_FrType':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, bytes):
            value = cls.bytes_to_int(py_obj)
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = cls.bytes_to_int(bytes.fromhex(py_obj))
        else:
            assert False, f'unexpected value {py_obj}'
        return cls.from_value(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'IntType':
        value = parse_micheline_literal(val_expr, {
            'int': int,
            'bytes': lambda x: cls.bytes_to_int(bytes.fromhex(x))
        })
        return cls.from_value(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode == 'readable':
            return {'int': str(self.value)}
        else:
            return {'bytes': self.value.to_bytes(32, 'little').hex()}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return super(BLS12_381_FrType, self).to_python_object()


class BLS12_381_G1Type(BytesType, prim='bls12_381_g1'):

    @classmethod
    def from_value(cls, value: bytes):
        assert len(value) == 96, f'expected 98 bytes, got {len(value)}'
        return cls(value)

    @classmethod
    def from_point(cls, point: G1Uncompressed) -> 'BLS12_381_G1Type':
        if bls12_381.is_inf(point):
            x, y = POW_2_382, 0
        else:
            x_pt, y_pt = bls12_381.normalize(point)
            x, y = x_pt.n, y_pt.n
        value = x.to_bytes(48, 'big') + y.to_bytes(48, 'big')
        return cls.from_value(value)

    def to_point(self) -> G1Uncompressed:
        x = int.from_bytes(self.value[:48], 'big')
        y = int.from_bytes(self.value[48:], 'big')
        point = FQ(x), FQ(y), FQ(1)
        return cast(G1Uncompressed, point)

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return super(BLS12_381_G1Type, self).to_python_object()


class BLS12_381_G2Type(BytesType, prim='bls12_381_g2'):

    @classmethod
    def from_value(cls, value: bytes):
        assert len(value) == 192, f'expected 98 bytes, got {len(value)}'
        return cls(value)

    @classmethod
    def from_point(cls, point: G2Uncompressed) -> 'BLS12_381_G2Type':
        if bls12_381.is_inf(point):
            x_re, x_im, y_re, y_im = 0, POW_2_382, 0, 0
        else:
            x, y = bls12_381.normalize(point)
            x_re, x_im = x.coeffs
            y_re, y_im = y.coeffs
        value = x_im.to_bytes(48, 'big') + x_re.to_bytes(48, 'big') \
            + y_im.to_bytes(48, 'big') + y_re.to_bytes(48, 'big')
        return cls(value)

    def to_point(self) -> G2Uncompressed:
        x_im = int.from_bytes(self.value[:48], 'big')
        x_re = int.from_bytes(self.value[48:96], 'big')
        y_im = int.from_bytes(self.value[96:144], 'big')
        y_re = int.from_bytes(self.value[144:192], 'big')
        point = FQ2([x_re, x_im]), FQ2([y_re, y_im]), FQ2([1, 0])
        return cast(G2Uncompressed, point)

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return super(BLS12_381_G2Type, self).to_python_object()
