from pytezos.encoding import forge_array, parse_array

prim_tags = {
    'parameter': b'\x00',
    'storage': b'\x01',
    'code': b'\x02',
    'False': b'\x03',
    'Elt': b'\x04',
    'Left': b'\x05',
    'None': b'\x06',
    'Pair': b'\x07',
    'Right': b'\x08',
    'Some': b'\x09',
    'True': b'\x0A',
    'Unit': b'\x0B',
    'PACK': b'\x0C',
    'UNPACK': b'\x0D',
    'BLAKE2B': b'\x0E',
    'SHA256': b'\x0F',
    'SHA512': b'\x10',
    'ABS': b'\x11',
    'ADD': b'\x12',
    'AMOUNT': b'\x13',
    'AND': b'\x14',
    'BALANCE': b'\x15',
    'CAR': b'\x16',
    'CDR': b'\x17',
    'CHECK_SIGNATURE': b'\x18',
    'COMPARE': b'\x19',
    'CONCAT': b'\x1A',
    'CONS': b'\x1B',
    '__CREATE_ACCOUNT__': b'\x1C',  # DEPRECATED
    'CREATE_CONTRACT': b'\x1D',
    'IMPLICIT_ACCOUNT': b'\x1E',
    'DIP': b'\x1F',
    'DROP': b'\x20',
    'DUP': b'\x21',
    'EDIV': b'\x22',
    'EMPTY_MAP': b'\x23',
    'EMPTY_SET': b'\x24',
    'EQ': b'\x25',
    'EXEC': b'\x26',
    'FAILWITH': b'\x27',
    'GE': b'\x28',
    'GET': b'\x29',
    'GT': b'\x2A',
    'HASH_KEY': b'\x2B',
    'IF': b'\x2C',
    'IF_CONS': b'\x2D',
    'IF_LEFT': b'\x2E',
    'IF_NONE': b'\x2F',
    'INT': b'\x30',
    'LAMBDA': b'\x31',
    'LE': b'\x32',
    'LEFT': b'\x33',
    'LOOP': b'\x34',
    'LSL': b'\x35',
    'LSR': b'\x36',
    'LT': b'\x37',
    'MAP': b'\x38',
    'MEM': b'\x39',
    'MUL': b'\x3A',
    'NEG': b'\x3B',
    'NEQ': b'\x3C',
    'NIL': b'\x3D',
    'NONE': b'\x3E',
    'NOT': b'\x3F',
    'NOW': b'\x40',
    'OR': b'\x41',
    'PAIR': b'\x42',
    'PUSH': b'\x43',
    'RIGHT': b'\x44',
    'SIZE': b'\x45',
    'SOME': b'\x46',
    'SOURCE': b'\x47',
    'SENDER': b'\x48',
    'SELF': b'\x49',
    'STEPS_TO_QUOTA': b'\x4A',
    'SUB': b'\x4B',
    'SWAP': b'\x4C',
    'TRANSFER_TOKENS': b'\x4D',
    'SET_DELEGATE': b'\x4E',
    'UNIT': b'\x4F',
    'UPDATE': b'\x50',
    'XOR': b'\x51',
    'ITER': b'\x52',
    'LOOP_LEFT': b'\x53',
    'ADDRESS': b'\x54',
    'CONTRACT': b'\x55',
    'ISNAT': b'\x56',
    'CAST': b'\x57',
    'RENAME': b'\x58',
    'bool': b'\x59',
    'contract': b'\x5A',
    'int': b'\x5B',
    'key': b'\x5C',
    'key_hash': b'\x5D',
    'lambda': b'\x5E',
    'list': b'\x5F',
    'map': b'\x60',
    'big_map': b'\x61',
    'nat': b'\x62',
    'option': b'\x63',
    'or': b'\x64',
    'pair': b'\x65',
    'set': b'\x66',
    'signature': b'\x67',
    'string': b'\x68',
    'bytes': b'\x69',
    'mutez': b'\x6A',
    'timestamp': b'\x6B',
    'unit': b'\x6C',
    'operation': b'\x6D',
    'address': b'\x6E',
    'SLICE': b'\x6F',
    'DIG': b'\x70',
    'DUG': b'\x71',
    'EMPTY_BIG_MAP': b'\x72',
    'APPLY': b'\x73',
    'chain_id': b'\x74',
    'CHAIN_ID': b'\x75'
}
prim_int = {v[0]: k for k, v in prim_tags.items()}

len_tags = [
    {
        False: b'\x03',
        True: b'\x04'
    },
    {
        False: b'\x05',
        True: b'\x06'
    },
    {
        False: b'\x07',
        True: b'\x08'
    },
    {
        False: b'\x09',
        True: b'\x09'
    }
]

reserved_entries = {
    'default': b'\x00',
    'root': b'\x01',
    'do': b'\x02',
    'set_delegate': b'\x03',
    'remove_delegate': b'\x04'
}


def forge_int(value: int):
    res = bytearray()
    i = abs(value)

    res.append((i & 0b00111111) | (0b11000000 if value < 0 else 0b10000000))
    i >>= 6

    while i != 0:
        res.append((i & 0b01111111) | 0b10000000)
        i >>= 7

    res[-1] &= 0b01111111
    return bytes(res)


def parse_int(data: bytes):
    value = 0
    length = 1

    while data[length - 1] & 0b10000000 != 0:
        length += 1

    for i in range(length - 1, 0, -1):
        value <<= 7
        value |= data[i] & 0b01111111

    value <<= 6
    value |= data[0] & 0b00111111

    if (data[0] & 0b01000000) != 0:
        value = -value

    return value, length


def forge_entrypoint(entrypoint):
    if entrypoint in reserved_entries:
        return reserved_entries[entrypoint]
    else:
        return b'\xff' + forge_array(entrypoint.encode(), len_bytes=1)


def forge_micheline(data):
    res = []

    if isinstance(data, list):
        res.append(b'\x02')
        res.append(forge_array(b''.join(map(forge_micheline, data))))

    elif isinstance(data, dict):
        if data.get('prim'):
            args_len = len(data.get('args', []))
            annots_len = len(data.get('annots', []))

            res.append(len_tags[args_len][annots_len > 0])
            res.append(prim_tags[data['prim']])

            if args_len > 0:
                args = b''.join(map(forge_micheline, data['args']))
                if args_len < 3:
                    res.append(args)
                else:
                    res.append(forge_array(args))

            if annots_len > 0:
                res.append(forge_array(' '.join(data['annots']).encode()))
            elif args_len == 3:
                res.append(b'\x00' * 4)

        elif data.get('bytes') is not None:
            res.append(b'\x0A')
            res.append(forge_array(bytes.fromhex(data['bytes'])))

        elif data.get('int') is not None:
            res.append(b'\x00')
            res.append(forge_int(int(data['int'])))

        elif data.get('string') is not None:
            res.append(b'\x01')
            res.append(forge_array(data['string'].encode()))
        else:
            assert False, data
    else:
        assert False, data

    return b''.join(res)


def forge_script(script):
    code = forge_micheline(script['code'])
    storage = forge_micheline(script['storage'])
    return forge_array(code) + forge_array(storage)


def unforge_micheline(data: bytes):
    ptr = 0

    def parse_list():
        nonlocal ptr
        _, offset = parse_array(data[ptr:])
        end, res = ptr + offset, []
        ptr += 4
        while ptr < end:
            res.append(parse())
        assert ptr == end, f'out of array boundaries'
        return res

    def parse_prim_expr(args_len=0, annots=False):
        nonlocal ptr
        prim_tag = data[ptr]
        ptr += 1
        expr = {'prim': prim_int[prim_tag]}

        if 0 < args_len < 3:
            expr['args'] = [parse() for _ in range(args_len)]
        elif args_len == 3:
            expr['args'] = parse_list()
        else:
            assert args_len == 0, f'unexpected args len {args_len}'

        if annots:
            value, offset = parse_array(data[ptr:])
            ptr += offset
            if len(value) > 0:
                expr['annots'] = value.decode().split(' ')

        return expr

    def parse():
        nonlocal ptr
        tag = data[ptr]
        ptr += 1
        if tag == 0:
            value, offset = parse_int(data[ptr:])
            ptr += offset
            return {'int': str(value)}
        elif tag == 1:
            value, offset = parse_array(data[ptr:])
            ptr += offset
            return {'string': value.decode()}
        elif tag == 2:
            return parse_list()
        elif tag == 3:
            return parse_prim_expr(args_len=0, annots=False)
        elif tag == 4:
            return parse_prim_expr(args_len=0, annots=True)
        elif tag == 5:
            return parse_prim_expr(args_len=1, annots=False)
        elif tag == 6:
            return parse_prim_expr(args_len=1, annots=True)
        elif tag == 7:
            return parse_prim_expr(args_len=2, annots=False)
        elif tag == 8:
            return parse_prim_expr(args_len=2, annots=True)
        elif tag == 9:
            return parse_prim_expr(args_len=3, annots=True)
        elif tag == 10:
            value, offset = parse_array(data[ptr:])
            ptr += offset
            return {'bytes': value.hex()}
        else:
            assert False, f'unkonwn tag {tag} at position {ptr}'

    return parse()
