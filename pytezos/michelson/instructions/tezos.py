from typing import List, cast, Tuple, Optional, Type

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.micheline import MichelineSequence
from pytezos.michelson.sections import ParameterSection
from pytezos.michelson.types.base import MichelsonType, Micheline
from pytezos.michelson.types import NatType, ContractType, AddressType, TimestampType, \
    OptionType, KeyHashType, UnitType, MutezType, OperationType, ChainIdType
from pytezos.context.execution import ExecutionContext


class AmountInstruction(MichelsonInstruction, prim='AMOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        amount = context.get_amount()
        res = MutezType.from_value(amount)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class BalanceInstruction(MichelsonInstruction, prim='BALANCE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        balance = context.get_balance()
        res = MutezType.from_value(balance)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class ChainIdInstruction(MichelsonInstruction, prim='CHAIN_ID'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        chain_id = context.get_chain_id()
        res = ChainIdType.from_value(chain_id)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


def get_entry_point_type(context: ExecutionContext, name: str, address=None) -> Optional[Type[MichelsonType]]:
    expr = context.get_parameter_expr(address)
    if expr is None:
        return None
    parameter = ParameterSection.match(expr)
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
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        res = type(cls.__name__, (cls,), dict(entry_point=get_entry_point_name(annots)))
        return cast(Type['MichelsonInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        self_type = get_entry_point_type(context, cls.entry_point)
        assert self_type, f'parameter type is not defined'
        self_address = context.get_self_address()
        res_type = ContractType.create_type(args=[self_type])
        res = res_type.from_value(f'{self_address}%{cls.entry_point}')
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SelfAddressInstruction(MichelsonInstruction, prim='SELF_ADDRESS'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: ExecutionContext):
        res = AddressType.from_value(context.get_self_address())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SenderInstruction(MichelsonInstruction, prim='SENDER'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        sender = context.get_sender()
        res = AddressType.from_value(sender)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SourceInstruction(MichelsonInstruction, prim='SOURCE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        source = context.get_source()
        res = AddressType.from_value(source)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class NowInstruction(MichelsonInstruction, prim='NOW'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        now = context.get_now()
        res = TimestampType.from_value(now)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class AddressInstruction(MichelsonInstruction, prim='ADDRESS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        contract = cast(ContractType, stack.pop1())
        contract.assert_type_in(ContractType)
        res = AddressType.from_value(contract.get_address())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [contract], [res]))
        return cls()


class ContractInstruction(MichelsonInstruction, prim='CONTRACT', args_len=1):
    entry_point: str

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        res = type(cls.__name__, (cls,), dict(entry_point=get_entry_point_name(annots)))
        return cast(Type['MichelsonInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        address = cast(AddressType, stack.pop1())
        address.assert_type_in(AddressType)
        entry_type = get_entry_point_type(context, cls.entry_point, address=str(address))
        contract_type = ContractType.create_type(args=cls.args)
        try:
            if entry_type is None:
                stdout.append(f'{cls.prim}: skip type checking for {str(address)}')
            else:
                entry_type.assert_type_equal(cls.args[0])
            res = OptionType.from_some(contract_type.from_value(f'{str(address)}%{cls.entry_point}'))
        except AssertionError:
            res = OptionType.none(contract_type)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [address], [res]))
        return cls()


class ImplicitAccountInstruction(MichelsonInstruction, prim='IMPLICIT_ACCOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        key_hash = cast(KeyHashType, stack.pop1())
        key_hash.assert_type_equal(KeyHashType)
        res = ContractType.create_type(args=[UnitType]).from_value(str(key_hash))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key_hash], [res]))
        return cls()


class CreateContractInstruction(MichelsonInstruction, prim='CREATE_CONTRACT', args_len=1):
    storage_type: Type[MichelsonType]

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        sequence = args[0]
        assert issubclass(sequence, MichelineSequence), f'expected sequence {{ parameter ; storage ; code }}'
        assert len(sequence.args) == 3, f'expected 3 sections, got {len(sequence.args)}'
        assert {arg.prim for arg in sequence.args} == {'parameter', 'storage', 'code'}, f'unexpected sections'
        storage = next(arg for arg in sequence.args if arg.prim == 'storage')
        return MichelsonInstruction.create_type(args=args,
                                                annots=annots,
                                                storage_type=storage.args[0])

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        delegate, amount, initial_storage = cast(Tuple[OptionType, MutezType, MichelsonType], stack.pop3())
        delegate.assert_type_equal(OptionType.create_type(args=[KeyHashType]))
        amount.assert_type_equal(MutezType)
        initial_storage.assert_type_equal(cls.storage_type)

        originated_address = AddressType.from_value(context.get_originated_address())
        context.spend_balance(int(amount))
        origination = OperationType.origination(
            source=context.get_self_address(),
            script=cls.args[0],
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        delegate = cast(OptionType, stack.pop1())
        delegate.assert_type_equal(OptionType.create_type(args=[KeyHashType]))

        delegation = OperationType.delegation(
            source=context.get_self_address(),
            delegate=None if delegate.is_none() else str(delegate.get_some())
        )
        stack.push(delegation)
        stdout.append(format_stdout(cls.prim, [delegate], [delegation]))
        return cls()


class TransferTokensInstruction(MichelsonInstruction, prim='TRANSFER_TOKENS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        parameter, amount, destination = cast(Tuple[MichelsonType, MutezType, ContractType], stack.pop3())
        amount.assert_type_equal(MutezType)
        assert isinstance(destination, ContractType), f'expected contract, got {destination.prim}'
        parameter.assert_type_equal(destination.args[0])

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


class VotingPowerInstruction(MichelsonInstruction, prim='VOTING_POWER'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: ExecutionContext):
        address = cast(KeyHashType, stack.pop1())
        address.assert_type_equal(KeyHashType)
        res = NatType.from_value(context.get_voting_power(str(address)))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [address], [res]))
        return cls()


class TotalVotingPowerInstruction(MichelsonInstruction, prim='TOTAL_VOTING_POWER'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: ExecutionContext):
        res = NatType.from_value(context.get_total_voting_power())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class LevelInstruction(MichelsonInstruction, prim='LEVEL'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: ExecutionContext):
        res = NatType.from_value(context.get_level())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()
