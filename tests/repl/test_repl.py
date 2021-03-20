import logging
from os.path import dirname
from os.path import join
from os import listdir
from unittest.case import TestCase

from pytezos import MichelsonRuntimeError
from pytezos.logging import logger
from pytezos.michelson.parse import MichelsonParser
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.repl import Interpreter
from pytezos.michelson.types import PairType, IntType

logger.setLevel(logging.DEBUG)


class InterpreterTest(TestCase):
    def test_execute(self) -> None:
        # Arrange
        interpreter = Interpreter()
        code = "PUSH int 1; PUSH int 2; PAIR"

        # Act
        result = interpreter.execute(code)

        # Assert
        self.assertEqual(None, result.error)
        self.assertEqual(
            [
                'PUSH / _ => 1',
                'PUSH / _ => 2',
                'PAIR / 2 : 1 => (2 * 1)',
            ],
            result.stdout,
        )
        self.assertEqual([PairType((IntType(2), IntType(1)))], interpreter.stack.items)

    def test_execute_rollback(self) -> None:
        # Arrange
        interpreter = Interpreter()
        code = "PUSH int 1; PUSH int 2; PAIR"
        bad_code = "PUSH int 1; PAIR; PAIR;"

        # Act
        interpreter.execute(code)
        result = interpreter.execute(bad_code)

        # Assert
        self.assertIsInstance(result.error, MichelsonRuntimeError)
        self.assertEqual(
            [
                'PUSH / _ => 1',
                'PAIR / 1 : (2 * 1) => (1 * (2 * 1))',
                'PAIR: got 1 items on the stack, want to pop 2',
            ],
            result.stdout,
        )
        self.assertEqual([PairType((IntType(2), IntType(1)))], interpreter.stack.items)
