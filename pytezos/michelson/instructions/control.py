from typing import List, cast, Tuple, Union, Type, Any

from pytezos.michelson.instructions.stack import PushInstruction
from pytezos.michelson.instructions.adt import PairInstruction
from pytezos.michelson.micheline import parse_micheline_literal, MichelsonSequence
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.types import MichelsonType, LambdaType, PairType, BoolType, ListType, OrType, OptionType, \
    MapType, SetType
from pytezos.michelson.stack import MichelsonStack
from pytezos.context.execution import ExecutionContext


def execute_dip(prim: str, stack: MichelsonStack, stdout: List[str],
                count: int, body: Type[MichelsonInstruction], context: ExecutionContext) -> MichelsonInstruction:
    stdout.append(format_stdout(prim, [f'<{count}>'], []))
    stack.protect(count=count)
    item = body.execute(stack, stdout, context=context)
    stack.restore(count=count)
    stdout.append(format_stdout(prim, [], [f'<{count}>']))
    return item


class DipnInstruction(MichelsonInstruction, prim='DIP', args_len=2):
    depth: int

    def __init__(self, item: MichelsonInstruction):
        super(DipnInstruction, self).__init__()
        self.item = item

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['DipnInstruction']:
        depth = parse_micheline_literal(args[0], {'int': int})
        res = type(cls.__name__, (cls,), dict(args=args, depth=depth, **kwargs))
        return cast(Type['DipnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        item = execute_dip(cls.prim, stack, stdout, count=cls.depth, body=cls.args[1], context=context)
        return cls(item)


class DipInstruction(MichelsonInstruction, prim='DIP', args_len=1):

    def __init__(self, item: MichelsonInstruction):
        super(DipInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        item = execute_dip(cls.prim, stack, stdout, count=1, body=cls.args[0], context=context)
        return cls(item)


class LambdaInstruction(MichelsonInstruction, prim='LAMBDA', args_len=3):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        res = LambdaType.create_type(args=cls.args[:2]).from_micheline_value(cls.args[2])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))


class ExecInstruction(MichelsonInstruction, prim='EXEC', args_len=3):

    def __init__(self, item: MichelsonInstruction):
        super(ExecInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        param, sub = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        assert isinstance(sub, LambdaType), f'expected lambda, got {sub.prim}'
        param.assert_type_equal(sub.args[0])
        sub_stack = MichelsonStack.from_items([param])
        sub_stdout = []
        sub_body = cast(MichelsonInstruction, sub.value)
        item = sub_body.execute(sub_stack, sub_stdout, context=context)
        res = sub_stack.pop1()
        res.assert_type_equal(sub.args[1])
        assert len(sub_stack) == 0, f'lambda stack is not empty {sub_stack}'
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [param, sub], [res]))
        stdout.extend(sub_stdout)
        return cls(item)


class ApplyInstruction(MichelsonInstruction, prim='APPLY'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        left, sub = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        sub.assert_type_in(LambdaType)
        sub.args[0].assert_type_in(PairType)
        left_type, right_type = sub.args[0].args
        left.assert_type_equal(left_type)

        value = MichelsonSequence.create_type(args=[
            PushInstruction.create_type(args=[left_type, left]),
            PairInstruction,
            sub.value
        ])
        res = LambdaType.create_type(args=[right_type, sub.args[1]])(value)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, sub], [res]))


class FailwithInstruction(MichelsonInstruction, prim='FAILWITH'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        a = stack.pop1()
        assert a.is_packable(), f'expected packable type, got {a.prim}'
        assert False, a


class IfInstruction(MichelsonInstruction, prim='IF', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        or_ = cast(OrType, stack.pop1())
        or_.assert_type_in(OrType)
        stdout.append(format_stdout(cls.prim, [or_], []))
        branch = cls.args[0] if or_.is_left() else cls.args[1]
        item = branch.execute(stack, stdout, context=context)
        return cls(item)


class IfNoneInstruction(MichelsonInstruction, prim='IF_NONE', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfNoneInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        src = cast(Union[ListType, MapType], stack.pop1())
        executions = []
        items = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb_leaves(list(elt))
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        src = cast(Union[ListType, MapType, SetType], stack.pop1())
        executions = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_comb_leaves(list(elt))
            stack.push(elt)
            stdout.append(format_stdout(cls.prim, popped, [elt]))
            execution = cls.args[0].execute(stack, stdout, context=context)
            executions.append(execution)
            popped = []
        return cls(executions)
