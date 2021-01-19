from typing import List, cast, Tuple, Union

from pytezos.michelson.instructions.stack import PushInstruction
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.types import MichelsonType, LambdaType, PairType, BoolType, ListType, OrType, OptionType, \
    MapType, SetType
from pytezos.michelson.stack import MichelsonStack


class InstructionSequence(MichelsonInstruction, args_len=None):

    def __init__(self, items: List[MichelsonInstruction]):
        super(InstructionSequence, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        items = [arg.execute(stack, stdout) for arg in cls.args]
        return cls(items)


class DipnInstruction(MichelsonInstruction, prim='DIP', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(DipnInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        depth = parse_micheline_literal(cls.args[0], {'int': int})
        stdout.append(format_stdout(cls.prim, [f'<{depth}>'], [f'<{depth}>']))
        stack.protect(depth)
        item = cls.args[1].execute(stack, stdout)
        stack.restore(depth)
        return cls(item)


class DipInstruction(MichelsonInstruction, prim='DIP'):

    def __init__(self, item: MichelsonInstruction):
        super(DipInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        stdout.append(format_stdout(cls.prim, [f'<1>'], [f'<1>']))
        stack.protect(1)
        item = cls.args[1].execute(stack, stdout)
        stack.restore(1)
        return cls(item)


class LambdaInstruction(MichelsonInstruction, prim='LAMBDA', args_len=3):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res = LambdaType.create_type(args=cls.args[:2]).from_micheline_value(cls.args[2])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))


class ExecInstruction(MichelsonInstruction, prim='EXEC', args_len=3):

    def __init__(self, item: MichelsonInstruction):
        super(ExecInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        param, sub = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        assert isinstance(sub, LambdaType), f'expected lambda, got {sub.prim}'
        param.assert_equal_types(sub.args[0])
        sub_stack = MichelsonStack.from_items([param])
        sub_stdout = []
        item = sub.value.execute(sub_stack, sub_stdout)
        res = sub_stack.pop1()
        res.assert_equal_types(sub.args[1])
        assert len(sub_stack) == 0, f'lambda stack is not empty {sub_stack}'
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [param, sub], [res]))
        stdout.extend(sub_stdout)
        return cls(item)


class ApplyInstruction(MichelsonInstruction, prim='APPLY'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        left, sub = cast(Tuple[MichelsonType, LambdaType], stack.pop2())
        assert isinstance(sub, LambdaType), f'expected lambda, got {sub.prim}'
        assert isinstance(sub.args[0], PairType), f'expected pair, got {sub.args[0].prim}'
        left_type, right_type = sub.args[0].args
        left.assert_equal_types(left_type)

        value = InstructionSequence.create_type(args=[
            PushInstruction.create_type(args=[left_type, left]),
            PairInstruction,
            sub.value
        ])
        res = LambdaType.create_type(args=[right_type, sub.args[1]])(value)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, sub], [res]))


class FailwithInstruction(MichelsonInstruction, prim='FAILWITH'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        a = stack.pop1()
        assert not a.is_big_map_friendly(), f'big_map or sapling_state type not expected here'
        assert False, a


class IfInstruction(MichelsonInstruction, prim='IF', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        cond = cast(BoolType, stack.pop1())
        cond.assert_equal_types(BoolType)
        stdout.append(format_stdout(cls.prim, [cond], []))
        branch = cls.args[0] if bool(cond) else cls.args[1]
        item = branch.execute(stack, stdout)
        return cls(item)


class IfConsInstruction(MichelsonInstruction, prim='IF_CONS', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfConsInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        lst = cast(ListType, stack.pop1())
        assert isinstance(lst, ListType), f'expected list, got {lst.prim}'
        if len(lst) > 0:
            head, tail = lst.split_head()
            stack.push(tail)
            stack.push(head)
            stdout.append(format_stdout(cls.prim, [lst], [head, tail]))
            branch = cls.args[0]
        else:
            stdout.append(format_stdout(cls.prim, [lst], []))
            branch = cls.args[1]
        item = branch.execute(stack, stdout)
        return cls(item)


class IfLeftInstruction(MichelsonInstruction, prim='IF_LEFT', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfLeftInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        or_ = cast(OrType, stack.pop1())
        assert isinstance(or_, OrType), f'expected or, got {or_.prim}'
        stdout.append(format_stdout(cls.prim, [or_], []))
        branch = cls.args[0] if or_.is_left() else cls.args[1]
        item = branch.execute(stack, stdout)
        return cls(item)


class IfNoneInstruction(MichelsonInstruction, prim='IF_NONE', args_len=2):

    def __init__(self, item: MichelsonInstruction):
        super(IfNoneInstruction, self).__init__()
        self.item = item

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        opt = cast(OptionType, stack.pop1())
        assert isinstance(opt, OptionType), f'expected option, got {opt.prim}'
        if opt.is_none():
            branch = cls.args[0]
            stdout.append(format_stdout(cls.prim, [opt], []))
        else:
            some = opt.get_some()
            stack.push(some)
            stdout.append(format_stdout(cls.prim, [opt], [some]))
            branch = cls.args[1]
        item = branch.execute(stack, stdout)
        return cls(item)


class LoopInstruction(MichelsonInstruction, prim='LOOP', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(LoopInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        items = []
        while True:
            cond = cast(BoolType, stack.pop1())
            cond.assert_equal_types(BoolType)
            stdout.append(format_stdout(cls.prim, [cond], []))
            if bool(cond):
                item = cls.args[0].execute(stack, stdout)
                items.append(item)
            else:
                break
        return cls(items)


class LoopLeftInstruction(MichelsonInstruction, prim='LOOP_LEFT', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(LoopLeftInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        items = []
        while True:
            or_ = cast(OrType, stack.pop1())
            assert isinstance(or_, OrType), f'expected or, got {or_.prim}'
            var = or_.resolve()
            stack.push(var)
            stdout.append(format_stdout(cls.prim, [or_], [var]))
            if or_.is_left():
                item = cls.args[0].execute(stack, stdout)
                items.append(item)
            else:
                break
        return cls(items)


class MapInstruction(MichelsonInstruction, prim='MAP', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(MapInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        src = cast(Union[ListType, MapType], stack.pop1())
        executions = []
        items = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_items(list(elt))
            stack.push(elt)
            stdout.append(format_stdout(cls.prim, popped, [elt]))
            execution = cls.args[0].execute(stack, stdout)
            executions.append(execution)
            new_elt = stack.pop1()
            if isinstance(src, MapType):
                items.append((elt[0], new_elt))
            else:
                items.append(new_elt)
            popped = [new_elt]
        res = type(src).from_items(items)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, popped, [res]))
        return cls(executions)


class IterInstruction(MichelsonInstruction, prim='ITER', args_len=1):

    def __init__(self, items: List[MichelsonInstruction]):
        super(IterInstruction, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        src = cast(Union[ListType, MapType, SetType], stack.pop1())
        executions = []
        popped = [src]
        for elt in src:
            if isinstance(src, MapType):
                elt = PairType.from_items(list(elt))
            stack.push(elt)
            stdout.append(format_stdout(cls.prim, popped, [elt]))
            execution = cls.args[0].execute(stack, stdout)
            executions.append(execution)
            popped = []
        return cls(executions)
