from unittest.case import TestCase
from unittest.mock import Mock, patch

from pytezos import ContractInterface
from pytezos.context.impl import ExecutionContext

from pytezos.michelson.sections import ParameterSection, StorageSection
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.micheline import MichelineSequence
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.program import MichelsonProgram
from pytezos.michelson.types import IntType, UnitType
from pytezos.rpc import ShellQuery, RpcNode


class JupyterInstructionsTest(TestCase):
    def setUp(self):
        self.context = ExecutionContext()
        self.stack = MichelsonStack()
        self.stdout = []

    def _execute_code(self, code, parameter=None, storage=None) -> None:
        micheline = michelson_to_micheline(code)
        sequence = MichelineSequence.match(micheline)

        program = MichelsonProgram.create(sequence)(
            'default', parameter or ParameterSection(UnitType()), storage or StorageSection(UnitType())
        )
        program.execute(self.stack, self.stdout, self.context)

    def test_dump(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 0 ;
                PUSH int 1 ;
                DUMP ;
            }
        """
        self._execute_code(code)

        self.assertEqual(
            [
                IntType(1),
                IntType(0),
            ],
            self.stack.items,
        )
        self.assertEqual(
            [
                'PUSH / _ => 0',
                'PUSH / _ => 1',
                'DUMP => [1, 0]',
            ],
            self.stdout,
        )

    def test_dump_value(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 0 ;
                PUSH int 1 ;
                DUMP 1;
            }
        """
        self._execute_code(code)

        self.assertEqual(
            [
                IntType(1),
                IntType(0),
            ],
            self.stack.items,
        )
        self.assertEqual(
            [
                'PUSH / _ => 0',
                'PUSH / _ => 1',
                'DUMP => [1]',
            ],
            self.stdout,
        )

    def test_print(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 0 ;
                PUSH int 1 ;
                PRINT "second in stack: {1}";
            }
        """
        self._execute_code(code)

        self.assertEqual(
            ['PUSH / _ => 0', 'PUSH / _ => 1', 'second in stack: 0'],
            self.stdout,
        )

    def test_debug(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                DEBUG 1;
            }
        """
        self._execute_code(code)

        self.assertEqual(True, self.context.debug)

    def test_drop_all(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 0 ;
                PUSH int 1 ;
                DROP_ALL;
            }
        """
        self._execute_code(code)

        self.assertEqual([], self.stack.items)
        self.assertEqual(
            [
                'PUSH / _ => 0',
                'PUSH / _ => 1',
            ],
            self.stdout,
        )

    def test_patch(self):
        code = """
            storage unit ;
            parameter unit ;
            code {
                PATCH AMOUNT 1;
                PATCH BALANCE 2;
                PATCH CHAIN_ID "ch21n1d";
                PATCH SENDER "test";
                PATCH SOURCE "test_test";
                PATCH NOW 1000000;
            }
        """
        self._execute_code(code)

        self.assertEqual(1, self.context.amount)
        self.assertEqual(2, self.context.balance)
        self.assertEqual('ch21n1d', self.context.chain_id)
        self.assertEqual('test', self.context.sender)
        self.assertEqual('test_test', self.context.source)
        self.assertEqual(1000000, self.context.now)

        code = """
            storage unit ;
            parameter unit ;
            code {
                PATCH AMOUNT;
                PATCH BALANCE;
                PATCH CHAIN_ID;
                PATCH SENDER;
                PATCH SOURCE;
                PATCH NOW "1970-01-01T00:00:01Z";
            }
        """
        self._execute_code(code)

        self.assertEqual(None, self.context.amount)
        self.assertEqual(None, self.context.balance)
        self.assertEqual(None, self.context.chain_id)
        self.assertEqual(None, self.context.sender)
        self.assertEqual(None, self.context.source)
        self.assertEqual(1, self.context.now)

    def test_reset(self):
        self.context.network = 'mainnet'
        self.context.chain_id = 'ch21n1d'
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 1;
                RESET;
            }
        """
        self._execute_code(code)

        self.assertEqual([], self.stack.items)
        self.assertEqual(None, self.context.network)
        self.assertEqual(None, self.context.chain_id)

    @patch('pytezos.rpc.node.RpcNode.get', Mock(return_value='some_chain_id'))
    def test_reset_value(self):
        self.context.shell = ShellQuery(RpcNode('https://rpc.tzkt.io/edonet'))
        self.context.network = 'mainnet'
        self.context.chain_id = 'ch21n1d'
        code = """
            storage unit ;
            parameter unit ;
            code {
                PUSH int 1;
                RESET "florencenet";
            }
        """
        self._execute_code(code)

        self.assertEqual([], self.stack.items)
        self.assertEqual('florencenet', self.context.network)
        self.assertEqual('some_chain_id', self.context.chain_id)
