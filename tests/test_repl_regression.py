from unittest import TestCase

from pytezos.repl.interpreter import Interpreter, StackItem
from pytezos.repl.control import assert_stack_type
from pytezos.repl.types import Option


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
