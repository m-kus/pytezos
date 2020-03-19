from typing import Dict
from simplejson import JSONDecodeError

from pytezos.interop import Interop
from pytezos.repl.types import StackItem, Map, BigMap
from pytezos.repl.parser import parse_expression, assert_expr_equal, get_int, assert_comparable, assert_big_map_val
from pytezos.michelson.pack import get_key_hash


def make_elt(args):
    assert isinstance(args, list) and len(args) == 2
    return {'prim': 'Elt', 'args': args}


def elt_to_update(elt, type_expr, big_map_id):
    key_hash = get_key_hash(elt['args'][0], type_expr['args'][0])
    update = {'action': 'update',
              'big_map': str(big_map_id),
              'key_hash': key_hash,
              'key': elt['args'][0],
              'value': elt['args'][1]}
    return key_hash, update


class BigMapPool:

    def __init__(self):
        self.maps = {}  # type: Dict[int, Map]
        self.tmp_id = -1
        self.alloc_id = 0
        self.maybe_remove = set()

    def reset(self):
        self.maps.clear()
        self.tmp_id = -1
        self.alloc_id = 0
        self.maybe_remove.clear()

    def empty(self, k_type_expr, v_type_expr) -> BigMap:
        assert_comparable(k_type_expr)
        assert_big_map_val(v_type_expr)
        res = BigMap(val=self.tmp_id,
                     val_expr={'int': str(self.tmp_id), '_diff': {}},
                     type_expr={'prim': 'big_map', 'args': [k_type_expr, v_type_expr]})
        self.tmp_id -= 1
        return res

    def _pre_alloc(self, val_expr, type_expr):
        res = {'int': str(self.tmp_id),
               '_diff': dict(elt_to_update(elt, type_expr, self.tmp_id) for elt in val_expr)}
        self.tmp_id -= 1
        return res

    def _check_allocated(self, val_expr, type_expr, network=None):
        big_map_id = get_int(val_expr)
        assert big_map_id >= 0, f'expected an allocated big map (>=0), got {big_map_id}'
        if big_map_id in self.maps:
            big_map = self.maps[big_map_id]
            _ = [assert_expr_equal(type_expr['args'][i], big_map.type_expr['args'][i]) for i in [0, 1]]
            return big_map_id, {'_diff': {}}
        else:
            assert network, f'big map #{big_map_id} is not allocated'
            self.alloc_id = max(self.alloc_id, big_map_id + 1)
            return big_map_id, {'_diff': {}, '_network': network}

    def _pre_copy(self, val_expr, type_expr, network=None):
        big_map_id, kw = self._check_allocated(val_expr, type_expr, network)
        res = {'int': str(self.tmp_id), '_copy': big_map_id, **kw}
        self.tmp_id -= 1
        return res

    def _pre_remove(self, val_expr, type_expr, network=None):
        big_map_id, kw = self._check_allocated(val_expr, type_expr, network)
        self.maybe_remove.add(big_map_id)
        return {'int': str(big_map_id), **kw}

    def pre_alloc(self, val_expr, type_expr, copy=False, network=None):
        def alloc_selector(val_node, type_node, res, type_path):
            prim = type_node['prim']
            if prim in ['list', 'set']:
                return res
            if prim in ['pair', 'or']:
                return {'prim': val_node['prim'], 'args': res}
            elif prim == 'option' and val_node['prim'] == 'Some':
                return {'prim': val_node['prim'], 'args': res}
            elif prim == 'map':
                return list(map(make_elt, res))
            elif prim == 'big_map':
                if isinstance(val_node, list):
                    return self._pre_alloc(val_node, type_node)
                elif copy:
                    return self._pre_copy(val_node, type_node, network=network)
                else:
                    return self._pre_remove(val_node, type_node, network=network)

            return val_node

        val_expr = parse_expression(val_expr, type_expr, alloc_selector)
        return StackItem.parse(val_expr=val_expr, type_expr=type_expr)

    def diff(self, storage: StackItem):
        res = []
        alloc_id = self.alloc_id
        maybe_remove = self.maybe_remove

        def diff_selector(val_node, type_node, val, type_path):
            nonlocal res, alloc_id, maybe_remove
            prim = type_node['prim']
            if prim in ['list', 'set']:
                return val
            if prim in ['pair', 'or']:
                return {'prim': val_node['prim'], 'args': val}
            elif prim == 'option' and val_node['prim'] == 'Some':
                return {'prim': val_node['prim'], 'args': val}
            elif prim == 'map':
                return list(map(make_elt, val))
            elif prim == 'big_map':
                assert isinstance(val, int), f'expected big map pointer'
                if val < 0:
                    big_map_id = alloc_id
                    if val_node.get('_copy'):
                        res.append({'action': 'copy',
                                    'source_big_map': str(val_node['_copy']),
                                    'destination_big_map': str(big_map_id)})
                    else:
                        res.append({'action': 'alloc',
                                    'big_map': str(big_map_id),
                                    'key_type': type_node['args'][0],
                                    'value_type': type_node['args'][1]})
                    alloc_id += 1
                else:
                    big_map_id = val
                    maybe_remove.remove(big_map_id)

                res.extend(map(lambda x: {**x, 'big_map': str(big_map_id)}, val_node['_diff'].values()))
                return {'int': str(big_map_id)}
            else:
                return val_node

        val_expr = parse_expression(storage.val_expr, storage.type_expr, diff_selector)
        res.extend([{'action': 'remove', 'big_map': x} for x in maybe_remove])
        return StackItem.parse(val_expr, storage.type_expr), res

    def commit(self, big_map_diff: list):
        for diff in big_map_diff:
            big_map_id = int(diff['big_map'])
            raw_map = self.maps.get(big_map_id)
            if diff['action'] == 'alloc':
                assert raw_map is None, f'#{big_map_id} already allocated'
                self.maps[big_map_id] = Map.empty(k_type_expr=diff['key_type'], v_type_expr=diff['value_type'])
            elif diff['action'] == 'remove':
                assert raw_map is not None, f'#{big_map_id} is not allocated'
                del self.maps[big_map_id]
            elif diff['action'] == 'update':
                assert raw_map is not None, f'#{big_map_id} is not allocated'
                key = raw_map.make_key(diff['key'])
                if diff.get('value'):
                    val = raw_map.make_val(diff['value'])
                    self.maps[big_map_id] = raw_map.update(key, val)
                else:
                    self.maps[big_map_id] = raw_map.remove(key)

        if big_map_diff:
            self.alloc_id = max([int(x['big_map']) for x in big_map_diff]) + 1
        self.maybe_remove.clear()

    def _get_big_map_val(self, big_map: BigMap, key: StackItem):
        key_hash = get_key_hash(key.val_expr, key.type_expr)
        network = big_map.val_expr['_network']
        try:
            res = Interop().using(network).shell.head.context.big_maps[int(big_map)][key_hash]()
        except JSONDecodeError:
            res = None
        return res

    def contains(self, big_map: BigMap, key: StackItem) -> bool:
        if key in big_map:
            return big_map.find(key) is not None
        if int(big_map) >= 0:
            if big_map.val_expr.get('_network'):
                v_val_expr = self._get_big_map_val(big_map, key)
                return v_val_expr is not None
            else:
                assert int(big_map) in self.maps, f'#{int(big_map)} is not allocated'
                return key in self.maps[int(big_map)]
        return False

    def find(self, big_map: BigMap, key: StackItem) -> 'StackItem':
        if key in big_map:
            return big_map.find(key)
        if int(big_map) >= 0:
            if big_map.val_expr.get('_network'):
                v_val_expr = self._get_big_map_val(big_map, key)
                if v_val_expr:
                    return StackItem.parse(val_expr=v_val_expr, type_expr=big_map.type_expr['args'][1])
            else:
                assert int(big_map) in self.maps, f'#{int(big_map)} is not allocated'
                return self.maps[int(big_map)].find(key)
