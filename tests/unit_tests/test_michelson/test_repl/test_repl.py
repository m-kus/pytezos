from unittest.case import TestCase, skip

from pytezos import MichelsonRuntimeError
from pytezos.michelson.instructions import CommitInstruction
from pytezos.michelson.repl import Interpreter
from pytezos.michelson.types import (
    PairType,
    IntType,
    UnitType,
    ListType,
    BigMapType,
    OperationType,
)


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
                "PUSH / _ => 1",
                "PUSH / _ => 2",
                "PAIR / 2 : 1 => (2 * 1)",
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
                "PUSH / _ => 1",
                "PAIR / 1 : (2 * 1) => (1 * (2 * 1))",
                "PAIR: got 1 items on the stack, want to pop 2",
            ],
            result.stdout,
        )
        self.assertEqual([PairType((IntType(2), IntType(1)))], interpreter.stack.items)

    def test_execute_contract(self) -> None:
        # Arrange
        interpreter = Interpreter()
        code = """
            storage unit ;
            parameter unit ;
            BEGIN Unit Unit ;
            DROP ;
            PUSH unit Unit ;
            NIL operation ;
            PAIR ;
            COMMIT ;
        """

        # Act
        result = interpreter.execute(code)

        # Assert
        self.assertEqual(None, result.error)
        self.assertEqual(
            [
                "storage: updated",
                "parameter: updated",
                "BEGIN %default / _ => (Unit * Unit)",
                "DROP / (Unit * Unit) => _",
                "PUSH / _ => Unit",
                "NIL / _ => []",
                "PAIR / [] : Unit => ([] * Unit)",
                "END %default / ([] * Unit) => _",
            ],
            result.stdout,
        )
        self.assertEqual(
            [],
            interpreter.stack.items,
        )

    def test_execute_contract_big_map(self) -> None:
        # Arrange
        interpreter = Interpreter()
        code = """
            storage (big_map string nat) ;
            parameter unit ;
            BEGIN Unit {};
                DROP ;
                EMPTY_BIG_MAP string nat ;
                PUSH nat 15 ;
                SOME ;
                PUSH string "cherry" ;
                UPDATE ;
                PUSH nat 22 ;
                SOME ;
                PUSH string "banana" ;
                UPDATE ;
                DUP ;
                PUSH string "cherry" ;
                DUP ;
                SWAP ;
                DIP { SWAP } ;
                MEM ;
                IF
                    { 
                        DIP { DUP } ;
                        DUP ;
                        DIP { SWAP } ;
                        GET ;
                        IF_SOME
                            { PUSH nat 5 ; ADD ; SOME ; SWAP ; UPDATE }
                            { DROP }
                    }
                    { DROP } ;
                NIL operation ;
                PAIR ;
            COMMIT ;
        """

        # Act
        result = interpreter.execute(code)

        # Assert
        self.assertEqual(None, result.error)
        self.assertEqual(
            [
                "storage: updated",
                "parameter: updated",
                "BEGIN %default / _ => (Unit * <-1>)",
                "DROP / (Unit * <-1>) => _",
                "EMPTY_BIG_MAP / _ => <-2>",
                "PUSH / _ => 15",
                "SOME / 15 => 15?",
                "PUSH / _ => 'cherry'",
                "UPDATE / 'cherry' : 15? : <-2> => <-2>",
                "PUSH / _ => 22",
                "SOME / 22 => 22?",
                "PUSH / _ => 'banana'",
                "UPDATE / 'banana' : 22? : <-2> => <-2>",
                "DUP / <-2> => <-2> : <-2>",
                "PUSH / _ => 'cherry'",
                "DUP / 'cherry' => 'cherry' : 'cherry'",
                "SWAP / 'cherry' : 'cherry' => 'cherry' : 'cherry'",
                "DIP / * => _",
                "SWAP / 'cherry' : <-2> => <-2> : 'cherry'",
                "DIP 1 / _ => *",
                "MEM / 'cherry' : <-2> => True",
                "IF / True => _",
                "DIP / * => _",
                "DUP / <-2> => <-2> : <-2>",
                "DIP 1 / _ => *",
                "DUP / 'cherry' => 'cherry' : 'cherry'",
                "DIP / * => _",
                "SWAP / 'cherry' : <-2> => <-2> : 'cherry'",
                "DIP 1 / _ => *",
                "GET / 'cherry' : <-2> => 15?",
                "IF_NONE / 15? => 15",
                "PUSH / _ => 5",
                "ADD / 5 : 15 => 20",
                "SOME / 20 => 20?",
                "SWAP / 20? : 'cherry' => 'cherry' : 20?",
                "UPDATE / 'cherry' : 20? : <-2> => <-2>",
                "NIL / _ => []",
                "PAIR / [] : <-2> => ([] * <-2>)",
                "END %default / ([] * <-2>) => _",
            ],
            result.stdout,
        )
        self.assertEqual(
            [],
            interpreter.stack.items,
        )
        self.assertEqual({}, interpreter.context.big_maps)
        commit_instruction = next(
            (
                i
                for i in result.instructions.items[::-1]
                if isinstance(i, CommitInstruction)
            )
        )
        self.assertEqual(
            [
                {
                    "diff": {
                        "action": "alloc",
                        "key_type": {"prim": "string"},
                        "updates": [
                            {
                                "key": {"string": "banana"},
                                "key_hash": "expruyWGhjeJ3v2cWgMkRyYuvbdZKjjARtHvhVeJDCyHgLebMmhBEo",
                                "value": {"int": "22"},
                            },
                            {
                                "key": {"string": "cherry"},
                                "key_hash": "expruVgSSodFW5ZDLidXaTVVczu6ddLVebXjMZBG33Z2oyQDUugvdE",
                                "value": {"int": "20"},
                            },
                        ],
                        "value_type": {"prim": "nat"},
                    },
                    "id": "0",
                    "kind": "big_map",
                }
            ],
            commit_instruction.lazy_diff,
        )

    def test_execute_contract_operations(self) -> None:
        # Arrange
        interpreter = Interpreter()
        code = """
            PATCH SENDER "tz1VSUr8wwNhLAzempoch5d6hLRiTh8Cjcjb" ;
            PATCH BALANCE 200 ;
            
            parameter mutez ;
            storage unit ;
            
            BEGIN 100 Unit ;
            
                CAR ;
                DUP ;
                BALANCE ;
                IFCMPLT
                    { FAIL }
                    {
                        SENDER ;
                        CONTRACT unit ;
                        IF_NONE
                            { FAIL }
                            {
                                SWAP ;
                                UNIT ;
                                TRANSFER_TOKENS ;
                                NIL operation ;
                                SWAP ;
                                CONS ;
                                UNIT ;
                                SWAP ;
                                PAIR
                            } ;
                    };
            COMMIT
        """

        # Act
        result = interpreter.execute(code)

        # Assert
        self.assertEqual(None, result.error)
        self.assertEqual(
            [
                "parameter: updated",
                "storage: updated",
                "BEGIN %default / _ => (0.0001 * Unit)",
                "CAR / (0.0001 * Unit) => 0.0001",
                "DUP / 0.0001 => 0.0001 : 0.0001",
                "BALANCE / _ => 0.0002",
                "COMPARE / 0.0002 : 0.0001 => 1",
                "LT / 1 => False",
                "IF / False => _",
                "SENDER / _ => tz1VSU…cjb",
                "CONTRACT: skip type checking for tz1VSUr8wwNhLAzempoch5d6hLRiTh8Cjcjb",
                "CONTRACT / tz1VSU…cjb => tz1VSU…cjb%default?",
                "IF_NONE / tz1VSU…cjb%default? => tz1VSU…cjb%default",
                "SWAP / tz1VSU…cjb%default : 0.0001 => 0.0001 : tz1VSU…cjb%default",
                "UNIT / _ => Unit",
                "TRANSFER_TOKENS / Unit : 0.0001 : tz1VSU…cjb%default => transaction",
                "NIL / _ => []",
                "SWAP / [] : transaction => transaction : []",
                "CONS / transaction : [] => [transaction]",
                "UNIT / _ => Unit",
                "SWAP / Unit : [transaction] => [transaction] : Unit",
                "PAIR / [transaction] : Unit => ([transaction] * Unit)",
                "END %default / ([transaction] * Unit) => _",
            ],
            result.stdout,
        )
        commit_instruction = next(
            (
                i
                for i in result.instructions.items[::-1]
                if isinstance(i, CommitInstruction)
            )
        )
        self.assertEqual(
            PairType(
                (
                    ListType(
                        [
                            OperationType(
                                {
                                    "kind": "transaction",
                                    "source": "KT1BEqzn5Wx8uJrZNvuS9DVHmLvG9td3fDLi",
                                    "destination": "tz1VSUr8wwNhLAzempoch5d6hLRiTh8Cjcjb",
                                    "amount": "100",
                                    "parameters": {
                                        "entrypoint": "default",
                                        "value": {"prim": "Unit"},
                                    },
                                }
                            )
                        ]
                    ),
                    UnitType(),
                )
            ),
            commit_instruction.result,
        )
