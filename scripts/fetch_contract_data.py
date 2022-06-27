"""Fetch contract data for tests from BCD and TzKT APIs"""
import json
import logging
from os import makedirs
from os.path import dirname, exists, join
from typing import Any, Dict, List, Optional, Tuple

import requests

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from pytezos.logging import logger


TZKT_API = 'https://api.tzkt.io/v1'
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


def get_raw_operation(level: int, hash_: str, counter: str, entrypoint: str) -> Dict[str, Any]:
    url = f'{RPC_API}/chains/main/blocks/{level}/operations/3'
    block = _get(url).json()
    for item in block:
        if item['hash'] != hash_:
            continue
        for op in item['contents']:
            if counter == op['counter'] and op['parameters']['entrypoint'] == entrypoint:
                return {
                    'parameters': op['parameters'],
                    'storage': op['metadata']['operation_result']['storage'],
                    'lazy_storage_diff': op['metadata']['operation_result'].get('lazy_storage_diff', [])
                }

            for int_op in op['metadata'].get('internal_operation_results', ()):
                if 'parameters' in int_op and int_op['parameters']['entrypoint'] == entrypoint:
                    return {
                        'parameters': int_op['parameters'],
                        'storage': int_op['result']['storage'],
                        'lazy_storage_diff': int_op['result'].get('lazy_storage_diff', [])
                    }
    else:
        raise Exception(level, hash_, counter, entrypoint)


def get_contract_list(offset: int, limit: int) -> List[List[str]]:
    params: Dict[str, Any] = {
        'kind': 'smart_contract',
        'lastActivity.gt': 2200000,
        'select.values': 'address,alias,typeHash',
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

    return get_raw_operation(op['level'], op['hash'], str(op['counter']), entrypoint)


def normalize_alias(alias: Optional[str]) -> str:
    if not alias:
        return ''
    return alias.replace(' ', '_').replace('/', '_').replace(':', '_').replace('.', '_').replace('-', '_').lower()


def fetch_contract_samples(limit: int) -> None:
    contracts = get_contract_list(0, 10000)
    code_hashes = set()

    for address, alias, code_hash in contracts:
        if not alias:
            continue

        if code_hash in code_hashes:
            continue
        else:
            code_hashes.add(code_hash)

        name = normalize_alias(alias)
        logger.info('Processing contract %s', name)

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

        if len(code_hashes) >= limit:
            return


if __name__ == '__main__':
    fetch_contract_samples(25)
    logger.info('Done')
