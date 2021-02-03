from unittest import TestCase

from pytezos.michelson.repl import Interpreter, StackItem, MichelsonRuntimeError
from pytezos.michelson.instructions.control import assert_stack_type
from pytezos.michelson.instructions.types import Option
from pytezos.michelson.pack import unpack, pack


class TestREPLRegression(TestCase):

    def test_push_preserves_name(self):
        i = Interpreter()
        i.execute('PUSH @a int 1 ; PUSH @b int 2 ; SWAP')
        fst = i.ctx.stack[0]  # type: StackItem
        sec = i.ctx.stack[1]  # type: StackItem
        self.assertEqual("a", fst.name)
        self.assertEqual("b", sec.name)

    def test_slice(self):
        i = Interpreter()
        i.execute('PUSH string "" ; PUSH nat 0 ; DUP ; SLICE')
        top = i.ctx.stack[0]  # type: Option
        assert_stack_type(top, Option)
        self.assertTrue(top.is_none())

    def test_now_failed_parse_exception_type(self):
        i = Interpreter()
        with self.assertRaises(MichelsonRuntimeError):
            i.execute('PUSH timestamp "2020-06-17 10:00:00"')

    def test_patch_now_str(self):
        i = Interpreter()
        i.execute('PATCH NOW "2020-06-17T10:00:00Z"')
        i.execute('PATCH NOW 1593082373')

    def test_unpack_concat_nat(self):
        i = Interpreter()
        i.execute("""
            PUSH nat 33 ;
            PUSH nat 44 ;
            PACK ;
            SWAP ;
            PACK ;
            CONCAT ;
            UNPACK nat ;
        """)
        top = i.ctx.stack[0]  # type: Option
        assert_stack_type(top, Option)
        self.assertTrue(top.is_none())

    def test_if_right(self):
        i = Interpreter()
        i.execute("""
            PUSH nat 42 ;
            LEFT string ;
            IF_RIGHT { FAIL } {}
        """)

    def test_top_level_annots(self):
        i = Interpreter()
        with self.assertRaises(MichelsonRuntimeError):
            i.execute("""storage (int :s)""")

    def test_disallowed_field_annots(self):
        i = Interpreter()
        with self.assertRaises(MichelsonRuntimeError):
            i.execute("""storage (big_map (address %key) (mutez %balance))""")

    def test_single_var_annot(self):
        i = Interpreter()
        with self.assertRaises(MichelsonRuntimeError):
            i.execute("""PUSH @foo @bar nat 42""")

    def test_single_type_annot(self):
        i = Interpreter()
        with self.assertRaises(MichelsonRuntimeError):
            i.execute("""PUSH (nat :foo :bar) 42""")

    def test_dup_n_macro(self):
        i = Interpreter()
        i.execute("""
            PUSH nat 100500 ;
            PUSH nat 42 ;
            PUSH string "Hello" ;
            PUSH string "World" ;
            DUP 3 ;           
        """)
        top = i.ctx.stack[0]
        self.assertEqual(42, int(top))

    def test_contract_unpackable(self):
        type_expr = {'prim': 'contract', 'args': [{'prim': 'string'}]}
        data = pack(val_expr={'string': 'KT1KzoKR7v1HjF2JqfYAWFV2ihzmUVJsDqXy%hello'}, type_expr=type_expr)
        with self.assertRaises(AssertionError):
            unpack(data=data, type_expr=type_expr)
