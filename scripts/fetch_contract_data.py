"""Fetch contract data for tests from BCD and TzKT APIs"""
import json
from datetime import datetime
from os import makedirs
from os.path import dirname, exists, join
from typing import Any, Dict, Iterator

import requests

from pytezos.logging import logger

BCD_API = 'https://api.better-call.dev'
TZKT_API = 'https://api.tzkt.io/v1'
RPC_API = 'https://rpc.tzkt.io'

NETWORK = 'mainnet'
SINCE = int(datetime(2020, 6, 1, 0, 0).timestamp())


def write_test_data(path: str, name: str, data: Dict[str, Any]) -> None:
    with open(join(path, f'{name}.json'), 'w+') as f:
        f.write(json.dumps(data, indent=2))


def fetch_bcd_search_results(offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        'q': 'KT1',
        'i': 'contract',
        'n': NETWORK,
        'g': 1,
        's': SINCE,
        'o': offset,
    }
    return requests.get(
        f'{BCD_API}/v1/search',
        params=params,
    ).json()


def iter_bcd_contracts(max_count: int = 100) -> Iterator[Dict[str, Any]]:
    offset = 0
    while offset < max_count:
        res = fetch_bcd_search_results(offset)
        if len(res['items']) == 0:
            break
        for item in res['items']:
            yield item['body']
            offset += 1


def fetch_script(address: str) -> Dict[str, Any]:
    return requests.get(f'{RPC_API}/{NETWORK}/chains/main/blocks/head/context/contracts/{address}/script').json()


def fetch_entrypoints(address: str) -> Dict[str, Any]:
    return requests.get(f'{RPC_API}/{NETWORK}/chains/main/blocks/head/context/contracts/{address}/entrypoints').json()


def fetch_operation_result(
    level: int,
    hash_: str,
    counter: int,
    internal: bool,
    address: str,
):
    operations = requests.get(
        f'{TZKT_API}/operations/transactions?level.eq={level}&select=storage,parameter,diffs,hash,level,counter,internal'
    ).json()
    for op in operations:
        parameter = op.get('parameter') or {}
        if op['hash'] == hash_ and op['counter'] == counter and bool(parameter.get('entrypoint')) == (not internal):
            break
    else:
        raise Exception

    return {
        'parameters': parameter.get('value', {}),
        'storage': op['storage'],
        'big_map_diff': op.get('diffs', []),
    }


def fetch_bcd_operation(address, entrypoint):
    res = requests.get(
        f'{BCD_API}/v1/contract/{NETWORK}/{address}/operations',
        params={
            'status': 'applied',
            'entrypoints': entrypoint,
            'size': 1,
        },
    ).json()
    return next((op for op in res['operations'] if op['destination'] == address and op['entrypoint'] == entrypoint), None)


def normalize_alias(alias):
    return alias.replace(' ', '_').replace('/', '_').replace(':', '_').lower()


def fetch_contract_samples(max_count=100):
    contracts = iter_bcd_contracts(max_count=max_count)
    for contract in contracts:
        name = normalize_alias(contract.get('alias', '')) or contract['address']
        path = join(dirname(dirname(__file__)), 'tests', 'contract_tests', name)
        if exists(path):
            continue
        else:
            makedirs(path)
        script = fetch_script(contract['address'])
        write_test_data(path, '__script__', script)
        entrypoints = fetch_entrypoints(contract['address'])
        write_test_data(path, '__entrypoints__', entrypoints)
        for entrypoint in contract['entrypoints']:
            operation = fetch_bcd_operation(contract['address'], entrypoint)
            if operation:
                result = fetch_operation_result(
                    operation['level'],
                    operation['hash'],
                    operation['counter'],
                    operation['internal'],
                    contract['address'],
                )
                write_test_data(path, entrypoint, result)
        logger.info(name)


if __name__ == '__main__':
    fetch_contract_samples()
