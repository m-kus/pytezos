from typing import Any, Callable, Generator
from loguru import logger

from pytezos.rpc.node import RpcError
from pytezos.rpc.query import RpcQuery
from pytezos.tools.docstring import get_attr_docstring
from pytezos.encoding import is_bh


def find_state_change_intervals(head: int, last: int, get: Callable, equals: Callable,
                                step=60) -> Generator:
    succ_value = get(head)
    logger.debug(f'{succ_value} at head {head}')

    for level in range(head - step, last, -step):
        value = get(level)
        logger.debug(f'{value} at level {level}')

        if not equals(value, succ_value):
            logger.debug(f'{value} -> {succ_value} at ({level}, {level + step})')
            yield level + step, succ_value, level, value
            succ_value = value


def find_state_change(head: int, last: int, get: Callable, equals: Callable,
                      pred_value: Any) -> (int, Any):
    def bisect(start: int, end: int):
        if end == start + 1:
            return end, get(end)

        level = (end + start) // 2
        value = get(level)
        logger.debug(f'{value} at level {level}')

        if equals(value, pred_value):
            return bisect(level, end)
        else:
            return bisect(start, level)

    return bisect(last, head)


def walk_state_change_interval(head: int, last: int, get: Callable, equals: Callable,
                               head_value: Any, last_value: Any) -> Generator:
    level = last
    value = last_value
    while not equals(value, head_value):
        level, value = find_state_change(head, level, get, equals, pred_value=value)
        logger.debug(f'{last_value} -> {value} at {level}')
        yield level, value


def find_state_changes(head: int, last: int, get: Callable, equals: Callable,
                       step=60) -> Generator:
    state_change_intervals = find_state_change_intervals(head, last, get, equals, step)
    for int_head, int_head_value, int_tail, int_last_value in state_change_intervals:
        for change in walk_state_change_interval(int_head, int_tail, get, equals,
                                                 head_value=int_head_value,
                                                 last_value=int_last_value):
            yield change


class BlockSliceQuery(RpcQuery):

    def __init__(self, start: int, stop=None, **kwargs):
        super(BlockSliceQuery, self).__init__(**kwargs)
        self._start = start
        self._stop = stop or 'head'

    def __repr__(self):
        res = [
            super(BlockSliceQuery, self).__repr__(),
            f'\nBlock range\n`{self._start}` — `{self._stop}`',
            f'\n(){get_attr_docstring(BlockSliceQuery, "__call__")}'
        ]
        return '\n'.join(res)

    def __getitem__(self, item):
        """
        Get block by index
        :param item: Index inside given block range
        :return: BlockQuery
        """
        start, stop = self.get_range()
        if item >= 0:
            return self._getitem(start + item)
        else:
            return self._getitem(stop + item + 1)

    def __call__(self) -> list:
        """
        Get block hashes (base58) for this interval
        """
        if is_bh(self._stop):
            head = self._stop
        else:
            head = self._getitem(self._stop).hash()

        if self._start < 0:
            length = abs(self._start)
        else:
            header = self._getitem(self._stop).header()
            length = header['level'] - self._start + 1

        return super(BlockSliceQuery, self).__call__(length=length, head=head)

    def get_range(self):
        """
        Get block level range.
        """
        def get_level(x):
            if isinstance(x, int):
                if x < 0:
                    return self.head.level() + x
                elif x > 0:
                    return x
                else:
                    assert False
            else:
                return self._getitem(x).header()['level']

        return get_level(self._start), get_level(self._stop)

    def find_proposal_injection(self, proposal_id):
        """
        Find proposal injection.
        :param proposal_id: Proposal hash (base58)
        """
        last, head = self.get_range()
        level, _ = find_state_change(
            head=head - 1,  # proposals are empty at the last block
            last=last,
            get=lambda x: self._getitem(x).votes.proposals[proposal_id](),
            equals=lambda x, y: x == y,
            pred_value=0
        )
        votes = self._getitem(level).operations.find_votes(proposal_id)
        assert len(votes) == 1
        return votes

    def find_upvotes(self, proposal_id) -> Generator:
        """
       Find upvoting operations for the given proposal.
       :param proposal_id: Proposal hash (base58)
       :return: Generator (lazy)
       """
        last, head = self.get_range()
        state_changes = find_state_changes(
            head=head - 1,  # proposals are empty at the last block
            last=last,
            get=lambda x: self._getitem(x).votes.proposals[proposal_id](),
            equals=lambda x, y: x == y
        )
        for level, _ in state_changes:
            for upvote in self._getitem(level).operations.find_upvotes(proposal_id):
                yield upvote

    def find_ballots(self) -> Generator:
        """
        Find ballot operations for the current period.
        :return: Generator (lazy)
        """
        last, head = self.get_range()
        state_changes = find_state_changes(
                head=head - 1,  # ballots are empty at the last block
                last=last,
                get=lambda x: self._getitem(x).votes.ballots(),
                equals=lambda x, y: x == y
        )
        for level, _ in state_changes:
            for ballot in self._getitem(level).operations.find_ballots():
                yield ballot

    def find_origination(self, contract_id):
        """
        Find contract origination
        :param contract_id: Contract ID (KT-address)
        """
        def get_counter(x):
            try:
                return self._getitem(x).context.contracts[contract_id].counter()
            except RpcError:
                return None

        level, _ = find_state_change(
            head=self.head.level(),
            last=0,
            get=get_counter,
            equals=lambda x, y: x == y,
            pred_value=None
        )
        return self._getitem(level).operations.find_origination(contract_id)

    def find_operation(self, operation_group_hash):
        """
        Find operation by hash
        :param operation_group_hash: base58
        :return: dict
        """
        last, head = self.get_range()
        for block_level in range(head, max(1, last - 1), -1):
            try:
                return self._getitem(block_level).operations[operation_group_hash]()
            except StopIteration:
                continue

        raise StopIteration(operation_group_hash)

    
class PeriodQuery(RpcQuery):
    __pos_key__ = ''
    __val_key__ = ''

    def _get_item(self, item) -> BlockSliceQuery:
        lvl = self.head.metadata()['level']
        blocks_per_period = int((lvl['level'] - lvl[self.__pos_key__] - 1) / lvl[self.__val_key__])

        def get_range(x):
            if x > 0:
                start_lvl = (x - 1) * blocks_per_period + 1
            elif x < 0:
                start_lvl = (lvl[self.__val_key__] + x + 1) * blocks_per_period + 1
            else:
                assert False

            stop_lvl = start_lvl + blocks_per_period - 1
            if stop_lvl > lvl['level']:
                stop_lvl = None

            return start_lvl, stop_lvl

        if isinstance(item, slice):
            start, _ = get_range(item.start or 1)
            _, stop = get_range(item.stop or -1)
        elif isinstance(item, int):
            start, stop = get_range(item)
        else:
            raise NotImplementedError(item)

        return BlockSliceQuery(
            start=start,
            stop=stop,
            node=self.node,
            path=self._wild_path,
            params=self._params
        )


class CyclesQuery(PeriodQuery):
    __pos_key__ = 'cycle_position'
    __val_key__ = 'cycle'

    def __call__(self, **params):
        """
        Get current cycle
        """
        return self.head.cycle()

    def __getitem__(self, item) -> BlockSliceQuery:
        """
        Get block range by cycle/cycle range.
        :param item: Cycle number or range (slice), range start/stop can be empty or negative
        :return: BlockSliceQuery
        """
        return self._get_item(item)


class VotingPeriodsQuery(PeriodQuery):
    __pos_key__ = 'voting_period_position'
    __val_key__ = 'voting_period'

    def __call__(self, **params):
        """
        Get current voting period
        """
        return self.head.voting_period()

    def __getitem__(self, item) -> BlockSliceQuery:
        """
        Get block range by voting_period/voting_period range.
        :param item: Voting_period number or range (slice), range start/stop can be empty or negative
        :return: BlockSliceQuery
        """
        return self._get_item(item)
