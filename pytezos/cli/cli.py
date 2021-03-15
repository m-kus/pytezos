import sys
from glob import glob
from os.path import abspath, dirname, exists, join
from pprint import pformat
from typing import Optional

import click

from pytezos import ContractInterface, __version__, pytezos
from pytezos.cli.github import create_deployment, create_deployment_status
from pytezos.context.mixin import default_network  # type: ignore
from pytezos.logging import logger
from pytezos.michelson.types.base import generate_pydoc
from pytezos.operation.result import OperationResult
from pytezos.rpc.errors import RpcError

kernel_js_path = join(dirname(dirname(__file__)), 'assets', 'kernel.js')
kernel_json = {
    "argv": ['pytezos', 'kernel', 'run', "-file", "{connection_file}"],
    "display_name": "Michelson",
    "language": "michelson",
    "codemirror_mode": "michelson",
}


def make_bcd_link(network, address):
    return f'https://better-call.dev/{network}/{address}'


def get_contract(path):
    if path is None:
        files = glob('*.tz')
        if len(files) != 1:
            raise Exception('No contracts found in working directory, specify --path implicitly')
        contract = ContractInterface.from_file(abspath(files[0]))
    elif exists(path):
        contract = ContractInterface.from_file(path)
    else:
        network, address = path.split(':')
        contract = pytezos.using(shell=network).contract(address)
    return contract


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli(*_args, **_kwargs):
    pass


@cli.command(help='Manage contract storage')
@click.option('--action', '-a', type=str, help='One of `schema`, `default`.')
@click.option('--path', '-p', type=str, default=None, help='Path to the .tz file, or the following uri: <network>:<KT-address>')
@click.pass_context
def storage(_ctx, action: str, path: Optional[str]) -> None:
    contract = get_contract(path)
    if action == 'schema':
        logger.info(generate_pydoc(type(contract.storage.data), title='storage'))
    elif action == 'default':
        logger.info(pformat(contract.storage.dummy()))
    else:
        raise Exception('Action must be either `schema` or `default`')


@cli.command(help='Manage contract storage')
@click.option('--action', '-a', type=str, default='schema', help='One of `schema`')
@click.option('--path', '-p', type=str, default=None, help='Path to the .tz file, or the following uri: <network>:<KT-address>')
@click.pass_context
def parameter(_ctx, action: str, path: Optional[str]) -> None:
    contract = get_contract(path)
    if action == 'schema':
        logger.info(contract.parameter.__doc__)
    else:
        raise Exception('Action must be `schema`')


@cli.command(help='Activate and reveal key from the faucet file')
@click.option('--path', '-p', type=str, help='Path to the .json file downloaded from https://faucet.tzalpha.net/')
@click.option('--network', '-n', type=str, default=default_network, help='Default is edo2net')
@click.pass_context
def activate(_ctx, path: str, network: str) -> None:
    ptz = pytezos.using(key=path, shell=network)
    logger.info(
        'Activating %s in the %s',
        ptz.key.public_key_hash(),
        network,
    )

    if ptz.balance() == 0:
        try:
            opg = ptz.reveal().autofill().sign()
            logger.info('Injecting reveal operation:')
            logger.info(pformat(opg.json_payload()))
            opg.inject(_async=False)
        except RpcError as e:
            logger.critical(pformat(e))
            sys.exit(-1)
        else:
            logger.info('Activation succeeded! Claimed balance: %s ꜩ', ptz.balance())
    else:
        logger.info('Already activated')

    try:
        opg = ptz.reveal().autofill().sign()
        logger.info('Injecting reveal operation:')
        logger.info(pformat(opg.json_payload()))
        opg.inject(_async=False)
    except RpcError as e:
        logger.critical(pformat(e))
        sys.exit(-1)
    else:
        logger.info('Your key %s is now active and revealed', ptz.key.public_key_hash())


@cli.command(help='Deploy contract to the specified network')
@click.option('--path', '-p', type=str, help='Path to the .tz file')
@click.option('--storage', type=str, default=None, help='Storage in JSON format (not Micheline)')
@click.option('--network', '-n', type=str, default=default_network, help='Default is edo2net')
@click.option('--key', type=str, default=None)
@click.option('--github-repo-slug', type=str, default=None)
@click.option('--github-oauth-token', type=str, default=None)
@click.option('--dry-run', type=bool, default=False, help='Set this flag if you just want to see what would happen')
@click.pass_context
def deploy(
    _ctx,
    path: str,
    storage: Optional[str],  # pylint: disable=redefined-outer-name
    network: str,
    key: Optional[str],
    github_repo_slug: Optional[str],
    github_oauth_token: Optional[str],
    dry_run: bool,
):
    ptz = pytezos.using(shell=network, key=key)
    logger.info('Deploying contract using %s in the %s', ptz.key.public_key_hash(), network)

    contract = get_contract(path)
    try:
        opg = ptz.origination(script=contract.script(initial_storage=storage)).autofill().sign()
        logger.info('Injecting origination operation:')
        logger.info(pformat(opg.json_payload()))

        if dry_run:
            logger.info(pformat(opg.preapply()))
            sys.exit(0)
        else:
            opg = opg.inject(_async=False)
    except RpcError as e:
        logger.critical(pformat(e))
        sys.exit(-1)
    else:
        originated_contracts = OperationResult.originated_contracts(opg)
        if len(originated_contracts) != 1:
            raise Exception('Operation group must has exactly one originated contract')
        bcd_link = make_bcd_link(network, originated_contracts[0])
        logger.info('Contract was successfully deployed: %s', bcd_link)

        if github_repo_slug:
            deployment = create_deployment(
                github_repo_slug,
                github_oauth_token,
                environment=network,
            )
            logger.info(pformat(deployment))
            status = create_deployment_status(
                github_repo_slug,
                github_oauth_token,
                deployment_id=deployment['id'],
                state='success',
                environment=network,
                environment_url=bcd_link,
            )
            logger.info(status)


if __name__ == '__main__':
    cli(prog_name='pytezos')
