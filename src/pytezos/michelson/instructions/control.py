from typing import List, Tuple, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.adt import PairInstruction
from pytezos.michelson.instructions.base import MichelsonInstruction, Wildcard, format_stdout
from pytezos.michelson.instructions.stack import PushInstruction
from pytezos.michelson.micheline import MichelineSequence, MichelsonRuntimeError
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import BoolType, LambdaType, ListType, MapType, MichelsonType, OptionType, OrType, PairType, SetType


def execute_dip(prim: str, stack: MichelsonStack, stdout: List[str],
                count: int, body: Type[MichelsonInstruction], context: AbstractContext) -> MichelsonInstruction:
    stdout.append(format_stdout(prim, [*Wildcard.n(count)], []))
    stack.protect(count=count)
    item = body.execute(stack, stdout, context=context)
    stack.restore(count=count)
    stdout.append(format_stdout(prim, [], [*Wildcard.n(count)], count))
    return item


class DipnInstruction(MichelsonInstruction, prim='DIP', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(DipnInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int()  # type: ignore
        item = execute_dip(cls.prim, stack, stdout, count=depth, body=cls.args[1], context=context)  # type: ignore
        return cls(item)


class DipInstruction(MichelsonInstruction, prim='DIP', args_len=1):

    def __init__(self, item: MichelsonInstruction):
        super(DipInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        item = execute_dip(cls.prim, stack, stdout, count=1, body=cls.args[0], context=context)  # type: ignore
        return cls(item)


class LambdaInstruction(MichelsonInstruction, prim='LAMBDA', args_len=3):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        lambda_type = LambdaType.create_type(args=cls.args[:2])
        res = lambda_type(cls.args[2])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ExecInstruction(MichelsonInstruction, prim='EXEC'):

    def __init__(self, item: MichelsonInstruction):
        super(ExecInstruction, self).__init__(stack_items_added=1)
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        param, lambda_ = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        assert isinstance(lambda_, LambdaType), f'expected lambda, got {lambda_.prim}'
        param.assert_type_equal(lambda_.args[0])
        stdout.append(format_stdout(cls.prim, [param, lambda_], []))  # type: ignore
        lambda_stack = MichelsonStack.from_items([param])
        lambda_body = cast(MichelsonInstruction, lambda_.value)
        item = lambda_body.execute(lambda_stack, stdout, context=context)
        res = lambda_stack.pop1()
        res.assert_type_equal(lambda_.args[1])
        assert len(lambda_stack) == 0, f'lambda stack is not empty {lambda_stack}'
        stack.push(res)
        return cls(item)


class ApplyInstruction(MichelsonInstruction, prim='APPLY'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        left, lambda_ = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        lambda_.assert_type_in(LambdaType)
        lambda_.args[0].assert_type_in(PairType)
        left_type, right_type = lambda_.args[0].args
        left.assert_type_equal(left_type)

        new_value = MichelineSequence.create_type(args=[
            PushInstruction.create_type(args=[left_type, left.to_literal()]),
            PairInstruction,
            lambda_.value
        ])
        res = LambdaType.create_type(args=[right_type, lambda_.args[1]])(new_value)  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, lambda_], [res]))  # type: ignore
        return cls(stack_items_added=1)


class FailwithInstruction(MichelsonInstruction, prim='FAILWITH'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = stack.pop1()
        assert a.is_packable(), f'expected packable type, got {a.prim}'
        raise MichelsonRuntimeError(repr(a))


class IfInstruction(MichelsonInstruction, prim='IF', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        cond = cast(BoolType, stack.pop1())
        cond.assert_type_equal(BoolType)
        stdout.append(format_stdout(cls.prim, [cond], []))  # type: ignore
        branch = cls.args[0] if bool(cond) else cls.args[1]
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfConsInstruction(MichelsonInstruction, prim='IF_CONS', args_len=2):

    def __init__(self, stack_items_added: int, item: MichelsonInstruction):
        super(IfConsInstruction, self).__init__(stack_items_added)
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        lst = cast(ListType, stack.pop1())
        lst.assert_type_in(ListType)
        if len(lst) > 0:
            head, tail = lst.split_head()
            stack.push(tail)
            stack.push(head)
            stdout.append(format_stdout(cls.prim, [lst], [head, tail]))  # type: ignore
            branch = cls.args[0]
            stack_items_added = 2
        else:
            stdout.append(format_stdout(cls.prim, [lst], []))  # type: ignore
            branch = cls.args[1]
            stack_items_added = 0
        item = branch.execute(stack, stdout, context=context)
        return cls(stack_items_added, item)


class IfLeftInstruction(MichelsonInstruction, prim='IF_LEFT', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfLeftInstruction, self).__init__(stack_items_added=1)
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        or_ = cast(OrType, stack.pop1())
        or_.assert_type_in(OrType)
        branch = cls.args[0] if or_.is_left() else cls.args[1]
        res = or_.resolve()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [or_], [res]))  # type: ignore
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfNoneInstruction(MichelsonInstruction, prim='IF_NONE', args_len=2):

    def __init__(self, stack_items_added: int, item: MichelsonInstruction):
        super(IfNoneInstruction, self).__init__(stack_items_added)
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        opt = cast(OptionType, stack.pop1())
        opt.assert_type_in(OptionType)
        if opt.is_none():
            branch = cls.args[0]
            stdout.append(format_stdout(cls.prim, [opt], []))  # type: ignore
            stack_items_added = 0
        else:
            some = opt.get_some()
            stack.push(some)
            stdout.append(format_stdout(cls.prim, [opt], [some]))  # type: ignore
            branch = cls.args[1]
            stack_items_added = 1
        item = branch.execute(stack, stdout, context=context)
        return cls(stack_items_added, item)


class LoopInstruction(MichelsonInstruction, prim='LOOP', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(LoopInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        items = []
        while True:
            cond = cast(BoolType, stack.pop1())
            cond.assert_type_equal(BoolType)
            stdout.append(format_stdout(cls.prim, [cond], []))  # type: ignore
            if bool(cond):
                item = cls.args[0].execute(stack, stdout, context=context)
                items.append(item)
            else:
                break
        return cls(items)


class LoopLeftInstruction(MichelsonInstruction, prim='LOOP_LEFT', args_len=1):

    def __init__(self, stack_items_added: int, items: List[MichelsonInstruction]):
        super(LoopLeftInstruction, self).__init__(stack_items_added)
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stack_items_added = 0
        items = []
        while True:
            or_ = cast(OrType, stack.pop1())
            or_.assert_type_in(OrType)
            var = or_.resolve()
            stack.push(var)
            stack_items_added += 1
            stdout.append(format_stdout(cls.prim, [or_], [var]))  # type: ignore
            if or_.is_left():
                item = cls.args[0].execute(stack, stdout, context=context)
                items.append(item)
            else:
                break
        return cls(stack_items_added, items)


class MapInstruction(MichelsonInstruction, prim='MAP', args_len=1):

    def __init__(self, stack_items_added: int, items: List[MichelsonInstruction]):
        super(MapInstruction, self).__init__(stack_items_added)
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stack_items_added = 0
        src = cast(Union[ListType, MapType], stack.pop1())
        executions = []
        items = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb(list(elt))  # type: ignore
            stack.push(elt)  # type: ignore
            stack_items_added += 1
            stdout.append(format_stdout(cls.prim, popped, [elt]))  # type: ignore
            execution = cls.args[0].execute(stack, stdout, context=context)
            executions.append(execution)
            new_elt = stack.pop1()
            if isinstance(src, MapType):
                items.append((elt[0], new_elt))
            else:
                items.append(new_elt)  # type: ignore
            popped = [new_elt]  # type: ignore

        if items:
            res = type(src).from_items(items)  # type: ignore
        else:
            res = src  # TODO: need to deduce argument types
        stack.push(res)
        stack_items_added += 1
        stdout.append(format_stdout(cls.prim, popped, [res]))  # type: ignore
        return cls(stack_items_added, executions)


class IterInstruction(MichelsonInstruction, prim='ITER', args_len=1):

    def __init__(self, stack_items_added: int, items: List[MichelsonInstruction]):
        super(IterInstruction, self).__init__(stack_items_added)
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stack_items_added = 0
        src = cast(Union[ListType, MapType, SetType], stack.pop1())
        executions = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb(list(elt))  # type: ignore
            stack_items_added += 1
            stack.push(elt)  # type: ignore
            stdout.append(format_stdout(cls.prim, popped, [elt]))  # type: ignore
            execution = cls.args[0].execute(stack, stdout, context=context)
            executions.append(execution)
            popped = []
        return cls(stack_items_added, executions)
