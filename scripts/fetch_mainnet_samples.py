import requests
import logging
import json
from os import makedirs
from os.path import dirname, join, exists


def write_test_data(folder, name, data):
    with open(join(folder, f'{name}.json'), 'w+') as f:
        f.write(json.dumps(data, indent=2))


def fetch_bcd_search_results(since=1590969600, offset=0):
    return requests.get('https://api.better-call.dev/v1/search', params={
        'q': 'KT1',
        'i': 'contract',
        'n': 'mainnet',
        'g': 1,
        's': since,
        'o': offset
    }).json()


def iter_bcd_contracts(max_count=100):
    offset = 0
    while offset < max_count:
        res = fetch_bcd_search_results(offset=offset)
        if len(res['items']) == 0:
            break
        for item in res['items']:
            yield item['body']
            offset += 1


def fetch_script(address):
    return requests.get(
        f'https://rpc.tzkt.io/mainnet/chains/main/blocks/head/context/contracts/{address}/script').json()


def fetch_entrypoints(address):
    return requests.get(
        f'https://rpc.tzkt.io/mainnet/chains/main/blocks/head/context/contracts/{address}/entrypoints').json()


def fetch_operation_result(level, opg_hash, counter, internal, address):
    res = requests.get(
        f'https://rpc.tzkt.io/mainnet/chains/main/blocks/{level}/operations/3').json()
    opg = next(opg for opg in res if opg['hash'] == opg_hash)
    op = next(op for op in opg['contents'] if int(op['counter']) == int(counter))
    if internal:
        content = next(o for o in op['metadata']['internal_operation_results'] if o['destination'] == address)
        result = content['result']
    else:
        content = op
        result = op['metadata']['operation_result']
    return {
        'parameters': content.get('parameters', {}),
        'storage': result['storage'],
        'big_map_diff': result.get('big_map_diff', [])
    }


def fetch_bcd_operation(address, entrypoint):
    res = requests.get(
        f'https://api.better-call.dev/v1/contract/mainnet/{address}/operations?status=applied&entrypoints={entrypoint}&size=1'
    ).json()
    return next((op for op in res['operations'] if op['destination'] == address and op['entrypoint'] == entrypoint), None)


def normalize_alias(alias):
    return alias.replace(' ', '_').replace('/', '_').replace(':', '_').lower()


def fetch_mainnet_samples(max_count=100):
    contracts = iter_bcd_contracts(max_count=max_count)
    for contract in contracts:
        name = normalize_alias(contract.get('alias', '')) or contract['address']
        folder = join(dirname(dirname(__file__)), 'tests', 'mainnet', name)
        if exists(folder):
            continue
        else:
            makedirs(folder)
        script = fetch_script(contract['address'])
        write_test_data(folder, '__script__', script)
        entrypoints = fetch_entrypoints(contract['address'])
        write_test_data(folder, '__entrypoints__', entrypoints)
        for entrypoint in contract['entrypoints']:
            operation = fetch_bcd_operation(contract['address'], entrypoint)
            if operation:
                result = fetch_operation_result(operation['level'],
                                                operation['hash'],
                                                operation['counter'],
                                                operation['internal'],
                                                contract['address'])
                write_test_data(folder, entrypoint, result)
        print(name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    fetch_mainnet_samples(10)
