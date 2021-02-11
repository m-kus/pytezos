from typing import List, cast, Tuple, Union, Type

from pytezos.michelson.instructions.stack import PushInstruction
from pytezos.michelson.instructions.adt import PairInstruction
from pytezos.michelson.micheline import MichelineSequence, MichelsonRuntimeError, Micheline
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.types import MichelsonType, LambdaType, PairType, BoolType, ListType, OrType, OptionType, \
    MapType, SetType
from pytezos.michelson.stack import MichelsonStack
from pytezos.context.abstract import AbstractContext
from pytezos.michelson.instructions.base import Wildcard


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
        depth = cls.args[0].get_int()
        item = execute_dip(cls.prim, stack, stdout, count=depth, body=cls.args[1], context=context)
        return cls(item)


class DipInstruction(MichelsonInstruction, prim='DIP', args_len=1):

    def __init__(self, item: MichelsonInstruction):
        super(DipInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        item = execute_dip(cls.prim, stack, stdout, count=1, body=cls.args[0], context=context)
        return cls(item)


class LambdaInstruction(MichelsonInstruction, prim='LAMBDA', args_len=3):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        lambda_type = LambdaType.create_type(args=cls.args[:2])
        res = lambda_type(cls.args[2])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))


class ExecInstruction(MichelsonInstruction, prim='EXEC'):

    def __init__(self, item: MichelsonInstruction):
        super(ExecInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        param, lambda_ = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        assert isinstance(lambda_, LambdaType), f'expected lambda, got {lambda_.prim}'
        param.assert_type_equal(lambda_.args[0])
        stdout.append(format_stdout(cls.prim, [param, lambda_], []))
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
        res = LambdaType.create_type(args=[right_type, lambda_.args[1]])(new_value)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, lambda_], [res]))
        return cls()


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
        stdout.append(format_stdout(cls.prim, [cond], []))
        branch = cls.args[0] if bool(cond) else cls.args[1]
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfConsInstruction(MichelsonInstruction, prim='IF_CONS', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfConsInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        lst = cast(ListType, stack.pop1())
        lst.assert_type_in(ListType)
        if len(lst) > 0:
            head, tail = lst.split_head()
            stack.push(tail)
            stack.push(head)
            stdout.append(format_stdout(cls.prim, [lst], [head, tail]))
            branch = cls.args[0]
        else:
            stdout.append(format_stdout(cls.prim, [lst], []))
            branch = cls.args[1]
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfLeftInstruction(MichelsonInstruction, prim='IF_LEFT', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfLeftInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        or_ = cast(OrType, stack.pop1())
        or_.assert_type_in(OrType)
        branch = cls.args[0] if or_.is_left() else cls.args[1]
        res = or_.resolve()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [or_], [res]))
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfNoneInstruction(MichelsonInstruction, prim='IF_NONE', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfNoneInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        opt = cast(OptionType, stack.pop1())
        opt.assert_type_in(OptionType)
        if opt.is_none():
            branch = cls.args[0]
            stdout.append(format_stdout(cls.prim, [opt], []))
        else:
            some = opt.get_some()
            stack.push(some)
            stdout.append(format_stdout(cls.prim, [opt], [some]))
            branch = cls.args[1]
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


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
            stdout.append(format_stdout(cls.prim, [cond], []))
            if bool(cond):
                item = cls.args[0].execute(stack, stdout, context=context)
                items.append(item)
            else:
                break
        return cls(items)


class LoopLeftInstruction(MichelsonInstruction, prim='LOOP_LEFT', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(LoopLeftInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        items = []
        while True:
            or_ = cast(OrType, stack.pop1())
            or_.assert_type_in(OrType)
            var = or_.resolve()
            stack.push(var)
            stdout.append(format_stdout(cls.prim, [or_], [var]))
            if or_.is_left():
                item = cls.args[0].execute(stack, stdout, context=context)
                items.append(item)
            else:
                break
        return cls(items)


class MapInstruction(MichelsonInstruction, prim='MAP', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(MapInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        src = cast(Union[ListType, MapType], stack.pop1())
        executions = []
        items = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb(list(elt))
            stack.push(elt)
            stdout.append(format_stdout(cls.prim, popped, [elt]))
            execution = cls.args[0].execute(stack, stdout, context=context)
            executions.append(execution)
            new_elt = stack.pop1()
            if isinstance(src, MapType):
                items.append((elt[0], new_elt))
            else:
                items.append(new_elt)
            popped = [new_elt]

        if items:
            res = type(src).from_items(items)
        else:
            res = src  # TODO: need to deduce argument types
        stack.push(res)
        stdout.append(format_stdout(cls.prim, popped, [res]))
        return cls(executions)


class IterInstruction(MichelsonInstruction, prim='ITER', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(IterInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        src = cast(Union[ListType, MapType, SetType], stack.pop1())
        executions = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb(list(elt))
            stack.push(elt)
            stdout.append(format_stdout(cls.prim, popped, [elt]))
            execution = cls.args[0].execute(stack, stdout, context=context)
            executions.append(execution)
            popped = []
        return cls(executions)
