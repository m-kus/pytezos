from pytezos.repl.types import StackItem, Map, BigMap
from pytezos.repl.parser import parse_prim_expr, get_int


class BigMapPool:

    def __init__(self):
        self.big_maps = {}
        self.next_id = 0
        self.diff = []

    def _get_map(self, big_map_id: int) -> Map:
        big_map = self.big_maps.get(big_map_id)  # type: Map
        assert big_map is not None, f'big map #{big_map_id} is not found'
        return big_map

    def _alloc(self, val_expr, type_expr):
        self.big_maps[self.next_id] = Map(val_expr=val_expr, type_expr=type_expr)
        self.diff.append({
            'action': 'alloc',
            'big_map': self.next_id,
            'key_type': type_expr['args'][0],
            'value_type': type_expr['args'][1]
        })
        pointer = {'int': str(self.next_id)}
        self.next_id += 1
        return pointer

    def _copy(self, val_expr):
        src_big_map_id = get_int(val_expr)
        raw_map = self._get_map(src_big_map_id)
        self.big_maps[self.next_id] = raw_map.rename(annots=[])
        self.diff.append({
            'action': 'copy',
            'source_big_map': src_big_map_id,
            'destination_big_map': self.next_id
        })
        pointer = {'int': str(self.next_id)}
        self.next_id += 1
        return pointer

    def _update(self, big_map_id, key: StackItem, val: StackItem = None):
        self.diff.append({
            'action': 'update',
            'big_map': str(big_map_id),
            'key_hash': '',  # TODO
            'key': key.val_expr,
            'value': val.val_expr if val else None
        })

    def alloc(self, item: StackItem):
        def try_alloc(val_node, type_node):
            type_prim, type_args = parse_prim_expr(type_node)
            if type_prim == 'pair':
                val_node['args'] = [try_alloc(val_node['args'][i], type_args[i]) for i in [0, 1]]
            elif type_prim == 'option':
                if val_node['prim'] == 'Some':
                    val_node['args'] = [try_alloc(val_node['args'][0], type_args[0])]
            elif type_prim == 'or':
                type_idx = 0 if val_node['prim'] == 'Left' else 1
                val_node['args'] = [try_alloc(val_node['args'][0], type_args[type_idx])]
            elif type_prim in ['list', 'set']:
                val_node = [try_alloc(v, type_args[0]) for v in val_node]
            elif type_prim == 'map':
                val_node = [{'prim': 'Elt',
                             'args': [elt['args'][0], try_alloc(elt['args'][1], type_args[1])]}
                            for elt in val_node]
            elif type_prim == 'big_map':
                if isinstance(val_node, list):
                    val_node = self._alloc(val_node, type_node)
                else:
                    val_node = self._copy(val_node)

            return val_node

        val_expr = try_alloc(item.val_expr, item.type_expr)
        return StackItem.parse(val_expr=val_expr, type_expr=item.type_expr)

    def empty(self, k_type_expr, v_type_expr) -> BigMap:
        type_expr = {'prim': 'big_map', 'args': [k_type_expr, v_type_expr]}
        val_expr = self._alloc(val_expr=[], type_expr=type_expr)
        return BigMap(val_expr=val_expr, type_expr=type_expr)

    def contains(self, big_map: BigMap, item: StackItem) -> bool:
        raw_map = self._get_map(int(big_map))
        return item in raw_map

    def find(self, big_map: BigMap, key: StackItem) -> 'StackItem':
        raw_map = self._get_map(int(big_map))
        return raw_map.find(key)

    def add(self, big_map: BigMap, key: StackItem, val: StackItem) -> 'BigMap':
        big_map_id = int(big_map)
        raw_map = self._get_map(big_map_id)
        self.big_maps[big_map_id] = raw_map.add(key, val)
        self._update(big_map_id, key, val)
        return big_map

    def remove(self, big_map: BigMap, key: StackItem) -> 'BigMap':
        big_map_id = int(big_map)
        raw_map = self._get_map(big_map_id)
        self.big_maps[big_map_id] = raw_map.remove(key)
        self._update(big_map_id, key, val=None)
        return big_map
