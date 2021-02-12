from glob import glob
from os.path import abspath, dirname, join, exists
from pprint import pprint
import fire

from pytezos import pytezos, ContractInterface
from pytezos.rpc.errors import RpcError
from pytezos.operation.result import OperationResult
from pytezos.context.mixin import default_network
from pytezos.michelson.types.base import generate_pydoc
from pytezos.cli.github import create_deployment, create_deployment_status

kernel_js_path = join(dirname(dirname(__file__)), 'assets', 'kernel.js')
kernel_json = {
    "argv": ['pytezos', 'kernel', 'run', "-file", "{connection_file}"],
    "display_name": "Michelson",
    "language": "michelson",
    "codemirror_mode": "michelson"
}


def make_bcd_link(network, address):
    return f'https://better-call.dev/{network}/{address}'


def get_contract(path):
    if path is None:
        files = glob('*.tz')
        assert len(files) == 1
        contract = ContractInterface.from_file(abspath(files[0]))
    elif exists(path):
        contract = ContractInterface.from_file(path)
    else:
        network, address = path.split(':')
        contract = pytezos.using(shell=network).contract(address)
    return contract


class PyTezosCli:

    def storage(self, action, path=None):
        """ Manage contract storage.

        :param action: One of `schema`, `default`
        :param path: Path to the .tz file, or the following uri: <network>:<KT-address>
        """
        contract = get_contract(path)
        if action == 'schema':
            print(generate_pydoc(type(contract.storage.data), title='storage'))
        elif action == 'default':
            pprint(contract.storage.dummy())
        else:
            assert False, action

    def parameter(self, action, path=None):
        """ Manage contract parameter.

        :param action: One of `schema`
        :param path: Path to the .tz file, or the following uri: <network>:<KT-address>
        """
        contract = get_contract(path)
        if action == 'schema':
            print(contract.parameter.__doc__)
        else:
            assert False, action

    def activate(self, path, network=default_network):
        """ Activates and reveals key from the faucet file.

        :param path: Path to the .json file downloaded from https://faucet.tzalpha.net/
        :param network: Default is Babylonnet
        """
        ptz = pytezos.using(key=path, shell=network)
        print(f'Activating {ptz.key.public_key_hash()} in the {network}')

        if ptz.balance() == 0:
            try:
                opg = ptz.activate_account().autofill().sign()
                print(f'Injecting activation operation:')
                pprint(opg.json_payload())
                opg.inject(_async=False)
            except RpcError as e:
                pprint(e)
                exit(-1)
            else:
                print(f'Activation succeeded! Claimed balance: {ptz.balance()} ꜩ')
        else:
            print('Already activated')

        try:
            opg = ptz.reveal().autofill().sign()
            print(f'Injecting reveal operation:')
            pprint(opg.json_payload())
            opg.inject(_async=False)
        except RpcError as e:
            pprint(e)
            exit(-1)
        else:
            print(f'Your key {ptz.key.public_key_hash()} is now active and revealed')

    def deploy(self, path, storage=None, network=default_network, key=None,
               github_repo_slug=None, github_oauth_token=None, dry_run=False):
        """ Deploy contract to the specified network.

        :param path: Path to the .tz file
        :param storage: Storage in JSON format (not Micheline)
        :param network:
        :param key:
        :param github_repo_slug:
        :param github_oauth_token:
        :param dry_run: Set this flag if you just want to see what would happen
        """
        ptz = pytezos.using(shell=network, key=key)
        print(f'Deploying contract using {ptz.key.public_key_hash()} in the {network}')

        contract = get_contract(path)
        try:
            opg = ptz.origination(script=contract.script(initial_storage=storage)).autofill().sign()
            print(f'Injecting origination operation:')
            pprint(opg.json_payload())

            if dry_run:
                pprint(opg.preapply())
                exit(0)
            else:
                opg = opg.inject(_async=False)
        except RpcError as e:
            pprint(e)
            exit(-1)
        else:
            originated_contracts = OperationResult.originated_contracts(opg)
            assert len(originated_contracts) == 1
            bcd_link = make_bcd_link(network, originated_contracts[0])
            print(f'Contract was successfully deployed: {bcd_link}')

            if github_repo_slug:
                deployment = create_deployment(github_repo_slug, github_oauth_token,
                                               environment=network)
                pprint(deployment)
                status = create_deployment_status(github_repo_slug, github_oauth_token,
                                                  deployment_id=deployment['id'],
                                                  state='success',
                                                  environment=network,
                                                  environment_url=bcd_link)
                pprint(status)


def main():
    return fire.Fire(PyTezosCli)


if __name__ == '__main__':
    main()
