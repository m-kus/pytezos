from typing import List, cast, Tuple, Optional, Type

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.micheline import MichelsonSequence
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.interpreter.program import MichelsonProgram
from pytezos.michelson.sections import ParameterSection
from pytezos.michelson.types.base import MichelsonType, MichelsonPrimitive
from pytezos.michelson.types import NatType, StringType, ContractType, AddressType, TimestampType, \
    OptionType, KeyHashType, UnitType, MutezType, OperationType
from pytezos.context.base import NodeContext


class AmountInstruction(MichelsonInstruction, prim='AMOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        amount = context.get_operation_amount()
        res = NatType.from_value(amount)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class BalanceInstruction(MichelsonInstruction, prim='BALANCE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        balance = context.get_balance()
        res = NatType.from_value(balance)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class ChainIdInstruction(MichelsonInstruction, prim='CHAIN_ID'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        chain_id = context.get_chain_id()
        res = StringType.from_value(chain_id)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


def get_entry_point_type(context: NodeContext, name: str, address=None) -> Optional[Type[MichelsonType]]:
    parameter = ParameterSection.match(context.get_parameter_expr(address))
    if parameter is None:
        return None
    entry_points = parameter.list_entry_points()
    assert name in entry_points, f'unknown entrypoint {name}'
    return entry_points[name]


def get_entry_point_name(annots: List[str]) -> str:
    if annots:
        assert len(annots) == 1 and annots[0].startswith('%'), f'single field annotation allowed'
        return annots[0][1:]
    else:
        return 'default'


class SelfInstruction(MichelsonInstruction, prim='SELF'):
    entry_point: str

    @classmethod
    def create_type(cls,
                    args: List[Type['MichelsonPrimitive']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        return MichelsonInstruction.create_type(args, annots, entry_point=get_entry_point_name(annots))

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        self_type = get_entry_point_type(context, cls.entry_point)
        assert self_type, f'parameter type is not defined'
        self_address = context.get_self_address()
        res = ContractType.create_type(args=[self_type]).from_value(self_address)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SenderInstruction(MichelsonInstruction, prim='SENDER'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        sender = context.get_operation_sender()
        res = AddressType.from_value(sender)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SourceInstruction(MichelsonInstruction, prim='SENDER'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        source = context.get_operation_source()
        res = AddressType.from_value(source)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class NowInstruction(MichelsonInstruction, prim='NOW'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        now = context.get_now()
        res = TimestampType.from_value(now)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class AddressInstruction(MichelsonInstruction, prim='ADDRESS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        contract = cast(ContractType, stack.pop1())
        assert isinstance(contract, ContractType), f'expected contract, got {contract.prim}'
        res = AddressType.from_value(str(contract))  # TODO: strip field annotation?
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [contract], [res]))
        return cls()


class ContractInstruction(MichelsonInstruction, prim='CONTRACT', args_len=1):
    entry_point: str

    @classmethod
    def create_type(cls,
                    args: List[Type['MichelsonPrimitive']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        entry_point = get_entry_point_name(annots)
        assert issubclass(args[0], MichelsonType), f'expected Michelson type, got {args[0]}'
        return MichelsonInstruction.create_type(args, annots, entry_point=entry_point)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        address = cast(AddressType, stack.pop1())
        assert isinstance(address, AddressType), f'expected address, got {address.prim}'
        entry_type = get_entry_point_type(context, cls.entry_point, address=str(address))
        contract_type = ContractType.create_type(args=cls.args)
        try:
            if entry_type is None:
                stdout.append(f'{cls.prim}: skip type checking for {str(address)}')
            else:
                entry_type.assert_equal_types(cls.args[0])
            res = OptionType.from_some(contract_type.from_value(f'{str(address)}%{cls.entry_point}'))
        except AssertionError:
            res = OptionType.none(contract_type)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [address], [res]))
        return cls()


class ImplicitAccountInstruction(MichelsonInstruction, prim='IMPLICIT_ACCOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        key_hash = cast(KeyHashType, stack.pop1())
        key_hash.assert_equal_types(KeyHashType)
        res = ContractType.create_type(args=[UnitType]).from_value(str(key_hash))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key_hash], [res]))
        return cls()


class CreateContractInstruction(MichelsonInstruction, prim='CREATE_CONTRACT', args_len=1):
    program: Type[MichelsonProgram]

    @classmethod
    def create_type(cls,
                    args: List[Type['MichelsonPrimitive']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        seq = args[0]
        assert issubclass(seq, MichelsonSequence), f'expected sequence {{ parameter ; storage ; code }}'
        return MichelsonInstruction.create_type(args=args,
                                                annots=annots,
                                                program=MichelsonProgram.match(seq))

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        delegate, amount, initial_storage = cast(Tuple[OptionType, MutezType, MichelsonType], stack.pop3())
        delegate.assert_equal_types(OptionType.create_type(args=[KeyHashType]))
        amount.assert_equal_types(MutezType)
        initial_storage.assert_equal_types(cls.program.storage.args[0])

        originated_address = AddressType.from_value(context.get_originated_address())
        context.spend_balance(int(amount))
        origination = OperationType.origination(
            source=context.get_self_address(),
            program=cls.program,
            storage=initial_storage,
            balance=int(amount),
            delegate=None if delegate.is_none() else str(delegate.get_some())
        )

        stack.push(originated_address)
        stack.push(origination)
        stdout.append(format_stdout(cls.prim, [delegate, amount, initial_storage], [origination, originated_address]))
        return cls()


class SetDelegateInstruction(MichelsonInstruction, prim='SET_DELEGATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        delegate = cast(OptionType, stack.pop1())
        delegate.assert_equal_types(OptionType.create_type(args=[KeyHashType]))

        delegation = OperationType.delegation(
            source=context.get_self_address(),
            delegate=None if delegate.is_none() else str(delegate.get_some())
        )
        stack.push(delegation)
        stdout.append(format_stdout(cls.prim, [delegate], [delegation]))
        return cls()


class TransferTokensInstruction(MichelsonInstruction, prim='TRANSFER_TOKENS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        parameter, amount, destination = cast(Tuple[MichelsonType, MutezType, ContractType], stack.pop3())
        amount.assert_equal_types(MutezType)
        assert isinstance(destination, ContractType), f'expected contract, got {destination.prim}'
        parameter.assert_equal_types(destination.args[0])

        transaction = OperationType.transaction(
            source=context.get_self_address(),
            destination=destination.get_address(),
            amount=int(amount),
            entrypoint=destination.get_entrypoint(),
            parameter=parameter
        )
        stack.push(transaction)
        stdout.append(format_stdout(cls.prim, [parameter, amount, destination], [transaction]))
        return cls()
