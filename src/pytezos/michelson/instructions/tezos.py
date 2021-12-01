import logging
from typing import List, Optional, Tuple, Type, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.micheline import MichelineLiteral, MichelineSequence, MichelsonRuntimeError
from pytezos.michelson.sections import ParameterSection, StorageSection, ViewSection
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import (AddressType, ChainIdType, ContractType, KeyHashType, MutezType, NatType, OperationType, OptionType,
                                     PairType, TimestampType, UnitType)
from pytezos.michelson.types.base import MichelsonType


class AmountInstruction(MichelsonInstruction, prim='AMOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        amount = context.get_amount()
        res = MutezType.from_value(amount)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class BalanceInstruction(MichelsonInstruction, prim='BALANCE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        balance = context.get_balance()
        res = MutezType.from_value(balance)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ChainIdInstruction(MichelsonInstruction, prim='CHAIN_ID'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        chain_id = context.get_chain_id()
        res = ChainIdType.from_value(chain_id)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


def get_entrypoint_type(context: AbstractContext, name: str, address=None) -> Optional[Type[MichelsonType]]:
    expr = context.get_parameter_expr(address)
    if expr is None:
        return None
    parameter = ParameterSection.match(expr)
    entrypoints = parameter.list_entrypoints()
    assert name in entrypoints, f'unknown entrypoint {name}'
    return entrypoints[name]


class SelfInstruction(MichelsonInstruction, prim='SELF'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        entrypoint = next(iter(cls.field_names), 'default')
        self_type = get_entrypoint_type(context, entrypoint)
        assert self_type, f'parameter type is not defined'
        self_address = context.get_self_address()
        res_type = ContractType.create_type(args=[self_type])
        res = res_type.from_value(f'{self_address}%{entrypoint}')  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class SelfAddressInstruction(MichelsonInstruction, prim='SELF_ADDRESS'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: AbstractContext):
        res = AddressType.from_value(context.get_self_address())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class SenderInstruction(MichelsonInstruction, prim='SENDER'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        sender = context.get_sender()
        res = AddressType.from_value(sender)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class SourceInstruction(MichelsonInstruction, prim='SOURCE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        source = context.get_source()
        res = AddressType.from_value(source)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class NowInstruction(MichelsonInstruction, prim='NOW'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        now = context.get_now()
        res = TimestampType.from_value(now)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class AddressInstruction(MichelsonInstruction, prim='ADDRESS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        contract = cast(ContractType, stack.pop1())
        contract.assert_type_in(ContractType)
        res = AddressType.from_value(contract.get_address())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [contract], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ContractInstruction(MichelsonInstruction, prim='CONTRACT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        entrypoint = next(iter(cls.field_names), 'default')
        address = cast(AddressType, stack.pop1())
        address.assert_type_in(AddressType)
        entrypoint_type = get_entrypoint_type(context, entrypoint, address=str(address))
        contract_type = ContractType.create_type(args=cls.args)
        try:
            if entrypoint_type is None:
                stdout.append(f'{cls.prim}: skip type checking for {str(address)}')
            else:
                entrypoint_type.assert_type_equal(cls.args[0])
            res = OptionType.from_some(contract_type.from_value(f'{str(address)}%{entrypoint}'))  # type: ignore
        except AssertionError:
            res = OptionType.none(contract_type)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [address], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ImplicitAccountInstruction(MichelsonInstruction, prim='IMPLICIT_ACCOUNT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        key_hash = cast(KeyHashType, stack.pop1())
        key_hash.assert_type_equal(KeyHashType)
        res = ContractType.create_type(args=[UnitType]).from_value(str(key_hash))  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key_hash], [res]))  # type: ignore
        return cls(stack_items_added=1)


class CreateContractInstruction(MichelsonInstruction, prim='CREATE_CONTRACT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        sequence = cast(MichelineSequence, cls.args[0])
        assert len(sequence.args) == 3, f'expected 3 sections, got {len(sequence.args)}'
        assert {arg.prim for arg in sequence.args} == {'parameter', 'storage', 'code'}, f'unexpected sections'
        storage_type = cast(Type[MichelsonType], next(arg.args[0] for arg in sequence.args if arg.prim == 'storage'))

        delegate, amount, initial_storage = cast(Tuple[OptionType, MutezType, MichelsonType], stack.pop3())
        delegate.assert_type_equal(OptionType.create_type(args=[KeyHashType]))
        amount.assert_type_equal(MutezType)
        initial_storage.assert_type_equal(storage_type)

        originated_address = AddressType.from_value(context.get_originated_address())
        context.spend_balance(int(amount))
        origination = OperationType.origination(
            source=context.get_self_address(),
            script=cls.args[0],  # type: ignore
            storage=initial_storage,
            balance=int(amount),
            delegate=None if delegate.is_none() else str(delegate.get_some())
        )

        stack.push(originated_address)
        stack.push(origination)
        stdout.append(format_stdout(cls.prim, [delegate, amount, initial_storage], [origination, originated_address]))  # type: ignore
        return cls(stack_items_added=2)


class SetDelegateInstruction(MichelsonInstruction, prim='SET_DELEGATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        delegate = cast(OptionType, stack.pop1())
        delegate.assert_type_equal(OptionType.create_type(args=[KeyHashType]))

        delegation = OperationType.delegation(
            source=context.get_self_address(),
            delegate=None if delegate.is_none() else str(delegate.get_some())
        )
        stack.push(delegation)
        stdout.append(format_stdout(cls.prim, [delegate], [delegation]))  # type: ignore
        return cls(stack_items_added=1)


class TransferTokensInstruction(MichelsonInstruction, prim='TRANSFER_TOKENS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        parameter, amount, destination = cast(Tuple[MichelsonType, MutezType, ContractType], stack.pop3())
        amount.assert_type_equal(MutezType)
        assert isinstance(destination, ContractType), f'expected contract, got {destination.prim}'
        param_type = destination.args[0]
        parameter.assert_type_equal(param_type)

        ep_type = get_entrypoint_type(context, destination.get_entrypoint(), address=destination.get_address())
        if ep_type:
            parameter.assert_type_equal(ep_type, message='destination contract parameter')

        transaction = OperationType.transaction(
            source=context.get_self_address(),
            destination=destination.get_address(),
            amount=int(amount),
            entrypoint=destination.get_entrypoint(),
            value=parameter.to_micheline_value(),
            param_type=param_type
        )
        stack.push(transaction)
        stdout.append(format_stdout(cls.prim, [parameter, amount, destination], [transaction]))  # type: ignore
        return cls(stack_items_added=1)


class VotingPowerInstruction(MichelsonInstruction, prim='VOTING_POWER'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: AbstractContext):
        address = cast(KeyHashType, stack.pop1())
        address.assert_type_equal(KeyHashType)
        res = NatType.from_value(context.get_voting_power(str(address)))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [address], [res]))  # type: ignore
        return cls(stack_items_added=1)


class TotalVotingPowerInstruction(MichelsonInstruction, prim='TOTAL_VOTING_POWER'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: AbstractContext):
        res = NatType.from_value(context.get_total_voting_power())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class LevelInstruction(MichelsonInstruction, prim='LEVEL'):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: AbstractContext):
        res = NatType.from_value(context.get_level())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ViewInstruction(MichelsonInstruction, prim='VIEW', args_len=2):

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: AbstractContext):
        input_value, view_address = cast(Tuple[MichelsonType, AddressType], stack.pop2())

        name = cast(Type[MichelineLiteral], cls.args[0]).get_string()
        address: Optional[str] = str(view_address)
        if address == context.get_self_address():
            address = None
        else:
            # FIXME: spawn new context with patched BALANCE and others
            logging.warning('PyTezos does not support external views with BALANCE or other context-dependent opcodes')

        return_ty = cast(Type[MichelsonType], cls.args[1])

        result = context.get_view_result(address=address, name=name)
        if result is not None:
            logging.info('Using patched VIEW result')
            res = OptionType.from_some(return_ty.from_python_object(result))
        else:
            try:
                view_expr = context.get_view_expr(name, address=address)
                if view_expr is None:
                    raise MichelsonRuntimeError(f'Failed to load view {str(view_address)}%{name}')

                view_ty = ViewSection.match(view_expr)
                return_ty.assert_type_equal(view_ty.args[2], message=f'view {name} return type')
            except (MichelsonRuntimeError, AssertionError) as e:
                stdout.append(f'VIEW: {str(e)}')
                res = OptionType.none(return_ty)
            else:
                storage_expr = context.get_storage_value(address)
                storage_ty = StorageSection.match(context.get_storage_expr())
                storage_value = storage_ty.from_micheline_value(storage_expr).item

                parameter = PairType.from_comb([input_value, storage_value])
                view_stack = MichelsonStack([parameter])
                # FIXME: need to patch context.balance
                view_code = cast(MichelineSequence, view_ty.args[3])
                view_code.execute(view_stack, stdout, context)
                if len(view_stack) != 1:
                    raise MichelsonRuntimeError('Expected single item on the stack, got', view_stack)
                res = OptionType.from_some(view_stack.pop1())

        stack.push(res)
        stdout.append(format_stdout(cls.prim, [input_value, view_address], [res]))  # type: ignore
        return cls(stack_items_added=1)


class OpenChestInstruction(MichelsonInstruction, prim='OPEN_CHEST'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        raise NotImplementedError
