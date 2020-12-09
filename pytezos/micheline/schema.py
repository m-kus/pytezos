import functools
from os.path import join, dirname

parsers = {}


def primitive(prim, args_len=None):
    def register_primitive(func):
        parsers[prim] = (func, args_len)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return register_primitive


def parse_prim_expr(expr) -> tuple:
    assert isinstance(expr, dict), f'expected dict, got {type(expr).__name__}'
    assert 'prim' in expr, f'prim field is absent'
    return expr['prim'], expr.get('args', []), expr.get('annots', [])


def forward(type_expr, annots):
    assert isinstance(annots, list), f'expected list, got {annots}'
    return dict(prim=type_expr['prim'],
                args=type_expr.get('args', []),
                annots=type_expr.get('annots', []) + annots)


def parse_expression(type_expr, schema, type_path='/'):
    prim, args, annots = parse_prim_expr(type_expr)
    if prim in parsers:
        func, args_len = parsers[prim]
        if args_len is not None:
            assert len(args) == args_len, f'{prim}: expected {args_len} args, got {len(args)}'
        func(args, annots, schema, type_path)
    else:
        assert len(args) == 0, f'{prim}: unexpected args {len(args)}'
        schema[type_path] = dict(
            prim=prim,
            annots=annots
        )


@primitive('parameter', args_len=1)
def parse_parameter(args, annots, schema, type_path):
    parse_expression(forward(args[0], annots), schema, type_path)


@primitive('storage', args_len=1)
def parse_storage(args, annots, schema, type_path):
    parse_expression(forward(args[0], annots), schema, type_path)


@primitive('option', args_len=1)
def parse_option(args, annots, schema, type_path):
    arg_path = join(type_path, 'o')
    schema[type_path] = dict(
        prim='option',
        args=[arg_path]
    )
    parse_expression(forward(args[0], annots), schema, arg_path)


def _parse_iterable(prim, args, annots, schema, type_path):
    arg_path = join(type_path, prim[0])
    schema[type_path] = dict(
        prim=prim,
        args=[arg_path],
        annots=annots
    )
    parse_expression(args[0], schema, arg_path)


@primitive('list', args_len=1)
def parse_list(args, annots, schema, type_path):
    _parse_iterable('list', args, annots, schema, type_path)


@primitive('set', args_len=1)
def parse_set(args, annots, schema, type_path):
    _parse_iterable('set', args, annots, schema, type_path)


def _parse_map(prim, args, annots, schema, type_path):
    key_path, val_path = join(type_path, 'k'), join(type_path, 'v')
    schema[type_path] = dict(
        prim=prim,
        args=[key_path, val_path],
        annots=annots
    )
    parse_expression(args[0], schema, key_path)
    parse_expression(args[1], schema, val_path)


@primitive('map', args_len=2)
def parse_map(args, annots, schema, type_path):
    _parse_map('map', args, annots, schema, type_path)


@primitive('big_map', args_len=2)
def parse_big_map(args, annots, schema, type_path):
    _parse_map('map', args, annots, schema, type_path)


def _parse_struct(prim, args, annots, schema, type_path):
    args_paths = [join(type_path, str(i)) for i in range(len(args))]
    schema[type_path] = dict(
        prim=prim,
        args=args_paths,
        annots=annots
    )
    for i, arg in enumerate(args):
        parse_expression(arg, schema, args_paths[i])


def _is_struct_root(prim, schema, type_path):
    return type_path == '/' or schema[dirname(type_path)]['prim'] != prim


def _get_flat_args(node, schema) -> list:
    res = list()
    for arg_path in node.get('args', []):
        arg = schema[arg_path]
        if arg['prim'] == node['prim']:
            res.extend(_get_flat_args(arg, schema))
        else:
            res.append(arg_path)
    return res


def get_name(node, prefixes, default=None):
    annots = node.get('annots', [])
    assert isinstance(annots, list), f'expected list, got {annots}'
    for prefix in prefixes:
        name = next(filter(lambda x: x.startswith(prefix), annots), None)
        if name is not None:
            return name[1:]
    return default


def get_names(node, schema, prefixes):
    names, is_named = [], False
    for i, arg_path in enumerate(node.get('args', [])):
        name = get_name(schema[arg_path], prefixes)
        if name and name not in names:
            is_named = True
        else:
            name = f'{schema[arg_path]["prim"]}_{i}'
        names.append(name)
    return names, is_named


def _parse_union(schema, type_path):
    args_paths = _get_flat_args(schema[type_path], schema)
    args_names, _ = get_names(schema[type_path], schema, prefixes=['%'])
    is_enum = all(map(lambda x: schema[x]['prim'] == 'unit', args_paths))
    schema[type_path] = dict(
        prim='enum' if is_enum else 'union',
        args=args_paths,
        annots=schema[type_path]['annots'],
        names=args_names  # always named
    )
    for i, arg_path in enumerate(args_paths):
        schema[arg_path]['name'] = args_names[i]
        schema[arg_path]['idx'] = i


@primitive('or', args_len=2)
def parse_or(args, annots, schema, type_path):
    _parse_struct('or', args, annots, schema, type_path)
    if _is_struct_root('or', schema, type_path):
        _parse_union(schema, type_path)


def _parse_tuple(schema, type_path):
    args_paths = _get_flat_args(schema[type_path], schema)
    args_names, is_named = get_names(schema[type_path], schema, prefixes=['%', ':'])
    schema[type_path] = dict(
        prim='tuple',
        args=args_paths,
        annots=schema[type_path]['annots'],
        names=[] if is_named else args_names
    )
    for i, arg_path in enumerate(args_paths):
        if is_named:
            schema[arg_path]['name'] = args_names[i]
        schema[arg_path]['idx'] = i


@primitive('pair')
def parse_pair(args, annots, schema, type_path):
    _parse_struct('pair', args, annots, schema, type_path)
    if _is_struct_root('pair', schema, type_path) or len(annots) > 0:
        _parse_tuple(schema, type_path)


@primitive('contract', args_len=1)
def parse_contract(args, annots, schema, type_path):
    schema[type_path] = dict(
        prim='contract',
        annots=annots,
        param=args[0]
    )


@primitive('lambda', args_len=2)
def parse_lambda(args, annots, schema, type_path):
    schema[type_path] = dict(
        prim='lambda',
        annots=annots,
        param=args[0],
        ret=args[1]
    )


def build_schema(type_expr):
    """ Creates a higher-level schema out from a Micheline type

    :param type_expr: Micheline type expression
    :return: map <type path> => <type description>
    """
    schema = {}
    parse_expression(type_expr, schema)
    return schema
