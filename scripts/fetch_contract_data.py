"""Fetch contract data for tests from BCD and TzKT APIs"""
import json
import logging
import sys
from contextlib import suppress
from os import makedirs
from os.path import dirname, exists, join
from typing import Any, Dict, List, Optional, Tuple

import requests

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from pytezos.logging import logger

TZKT_API = 'https://api.tzkt.io/v1'
# RPC_API = 'https://rpc.tzkt.io/mainnet'
RPC_API = 'https://mainnet-tezos.giganode.io'


def _get(url: str, params: Optional[Dict[str, Any]] = None):
    logger.info(f'GET {url}?{"&".join(f"{k}={v}" for k, v in (params or {}).items())}')
    return requests.get(url, params=params)


def write_test_data(path: str, name: str, data: Dict[str, Any]) -> None:
    with open(join(path, f'{name}.json'), 'w+') as f:
        f.write(json.dumps(data, indent=2))


def get_raw_script(address: str) -> Dict[str, Any]:
    url = f'{RPC_API}/chains/main/blocks/head/context/contracts/{address}/script'
    return _get(url).json()


def get_raw_entrypoints(address: str) -> Dict[str, Any]:
    url = f'{RPC_API}/chains/main/blocks/head/context/contracts/{address}/entrypoints'
    return _get(url).json()


def get_raw_storage(address: str) -> Dict[str, Any]:
    url = f'{RPC_API}/chains/main/blocks/head/context/contracts/{address}/storage'
    return _get(url).json()


def get_raw_parameter(level: int, hash_: str, counter: str, entrypoint: str) -> Dict[str, Any]:
    url = f'{RPC_API}/chains/main/blocks/{level}/operations/3'
    block = _get(url).json()
    for item in block:
        if item['hash'] != hash_:
            continue
        for op in item['contents']:
            if counter == op['counter'] and op['parameters']['entrypoint'] == entrypoint:
                return op['parameters']

            for int_op in op['metadata'].get('internal_operation_results', ()):
                if 'parameters' in int_op and int_op['parameters']['entrypoint'] == entrypoint:
                    return int_op['parameters']
    else:
        raise Exception(level, hash_, counter, entrypoint)


def get_contract_list(offset: int, limit: int) -> List[List[str]]:
    params: Dict[str, Any] = {
        'kind': 'smart_contract',
        'select.values': 'address,alias',
        'sort.desc': 'id',
        'offset': offset,
        'limit': limit,
    }
    return _get(
        f'{TZKT_API}/contracts',
        params=params,
    ).json()


def get_contract_entrypoints(address: str) -> List[str]:
    result = _get(
        f'{TZKT_API}/contracts/{address}/entrypoints',
        params={'select': 'entrypoints'},
    ).json()
    return [c['name'] for c in result]


def get_contract_call(address: str, entrypoint: str) -> Optional[Dict[str, Any]]:
    url = f'{TZKT_API}/operations/transactions'
    params: Dict[str, Any] = {
        'select': 'level,hash,counter,diffs',
        'target': address,
        'entrypoint': entrypoint,
        'micheline': 2,
        'limit': 1,
    }

    try:
        op = _get(url, params=params).json()[0]
    except IndexError:
        return None

    op['parameter'] = get_raw_parameter(op['level'], op['hash'], str(op['counter']), entrypoint)
    op['storage'] = get_raw_storage(address)
    op['diffs'] = op['diffs'] or []

    # NOTE: TzKT doesn't set these fields
    for diff in op['diffs']:
        diff['kind'] = 'big_map'
        diff['id'] = diff['bigmap']

    return op


def normalize_alias(alias: Optional[str]) -> str:
    if not alias:
        return ''
    return alias.replace(' ', '_').replace('/', '_').replace(':', '_').lower()


def fetch_contract_samples(offset: int, limit: int, contracts: Optional[Tuple[Tuple[str, str], ...]] = None) -> None:
    for address, alias in contracts or get_contract_list(offset, limit):
        name = normalize_alias(alias) or address

        path = join(dirname(dirname(__file__)), 'tests', 'contract_tests', name)
        if exists(path):
            logger.info('Skipping contract `%s`', name)
            continue

        logger.info('Fetching contract `%s`', name)
        entrypoints = get_contract_entrypoints(address)
        entrypoint_data = []
        for entrypoint in entrypoints:
            logger.info('Fetching %s:%s operation', name, entrypoint)
            operation = get_contract_call(address, entrypoint)
            if not operation:
                continue

            operation = {
                'parameters': operation['parameter'],
                'storage': operation['storage'],
                'big_map_diff': operation['diffs'],
            }
            entrypoint_data.append((path, entrypoint, operation))

        if not entrypoint_data:
            logger.info('No operations found for `%s`, skipping', name)

        makedirs(path)

        raw_script = get_raw_script(address)
        write_test_data(path, '__script__', raw_script)

        raw_entrypoints = get_raw_entrypoints(address)
        write_test_data(path, '__entrypoints__', raw_entrypoints)

        for _path, _entrypoint, _operation in entrypoint_data:
            write_test_data(_path, _entrypoint, _operation)

        logger.info('Done')


if __name__ == '__main__':
    args = sys.argv[1:]
    contracts = ((args[0], args[1]),) if len(args) == 2 else None
    offset, limit = 40000, 10
    logger.info('Fetching contract samples; offset=%s, limit=%s', offset, limit)
    fetch_contract_samples(offset, limit, contracts)
