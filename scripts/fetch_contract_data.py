"""Fetch contract data for tests from BCD and TzKT APIs"""
from contextlib import suppress
import json
import logging
from os import makedirs
from os.path import dirname, exists, join
from typing import Any, Dict, List, Optional

import requests
from requests import JSONDecodeError


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from pytezos.logging import logger

TZKT_API = 'https://api.tzkt.io/v1'
RPC_API = 'https://rpc.tzkt.io'

NETWORK = 'mainnet'


def write_test_data(path: str, name: str, data: Dict[str, Any]) -> None:
    with open(join(path, f'{name}.json'), 'w+') as f:
        f.write(json.dumps(data, indent=2))


def get_contract_list(offset: int, limit: int) -> List[List[str]]:
    params: Dict[str, Any] = {
        'kind': 'smart_contract',
        'select.values': 'address,alias',
        'sort.desc': 'id',
        'offset': offset,
        'limit': limit,
    }
    return requests.get(
        f'{TZKT_API}/contracts',
        params=params,
    ).json()


def get_contract_entrypoints(address: str) -> List[str]:
    result = requests.get(
        f'{TZKT_API}/contracts/{address}/entrypoints',
        params={'select': 'entrypoints'},
    ).json()
    return [c['name'] for c in result]


def get_contract_call(address: str, entrypoint: str) -> Optional[Dict[str, Any]]:
    url = f'{TZKT_API}/operations/transactions'
    params: Dict[str, Any] = {
        'select': 'storage,parameter,diffs,hash,level,counter,target',
        'target': address,
        'entrypoint': entrypoint,
        'micheline': 2,
        'limit': 1,
    }
    with suppress(IndexError, JSONDecodeError):
        return requests.get(url, params=params).json()[0]
    return None


def get_raw_script(address: str) -> Dict[str, Any]:
    url = f'{RPC_API}/{NETWORK}/chains/main/blocks/head/context/contracts/{address}/script'
    return requests.get(url).json()


def get_raw_entrypoints(address: str) -> Dict[str, Any]:
    url = f'{RPC_API}/{NETWORK}/chains/main/blocks/head/context/contracts/{address}/entrypoints'
    return requests.get(url).json()


def normalize_alias(alias: Optional[str]) -> str:
    if not alias:
        return ''
    return alias.replace(' ', '_').replace('/', '_').replace(':', '_').lower()


def fetch_contract_samples(offset: int, limit: int) -> None:
    # [['KT1Tr2eG3eVmPRbymrbU2UppUmKjFPXomGG9', 'dexter_usdtz_xtz']]
    for address, alias in get_contract_list(offset, limit):
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

            operation['diffs'] = operation['diffs'] or []
            # NOTE: TzKT doesn't set this fields
            for diff in operation['diffs']:
                diff['kind'] = 'big_map'
                diff['id'] = diff['bigmap']

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
    offset, limit = 20000, 300
    logger.info('Fetching contract samples; offset=%s, limit=%s', offset, limit)
    fetch_contract_samples(offset, limit)
