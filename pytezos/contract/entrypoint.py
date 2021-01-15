from pytezos.contract.script import ContractScript
from pytezos.contract.call import ContractCall
from pytezos.interop import Interop


class ContractEntrypoint(Interop):
    """ Proxy class for spawning ContractCall instances.
    """

    def __init__(self, name, address=None, script: ContractScript = None, shell=None, key=None):
        super(ContractEntrypoint, self).__init__(shell=shell, key=key)
        if script is None:
            assert address is not None
            code = self.shell.contracts[address].code()
            script = ContractScript.from_micheline(code)

        self.script = script
        self.name = name
        self.address = address

    def _spawn(self, **kwargs):
        return ContractEntrypoint(
            name=self.name,
            script=self.script,
            address=self.address,
            shell=kwargs.get('shell', self.shell),
            key=kwargs.get('key', self.key),
        )

    def __repr__(self):
        res = [
            super(ContractEntrypoint, self).__repr__(),
            f'.address  # {self.address}',
            f'\n{self.__doc__}'
        ]
        return '\n'.join(res)

    def __call__(self, *args, **kwargs):
        """ Spawn a contract call proxy initialized with the entrypoint name

        :param args: entrypoint args
        :param kwargs: entrypoint key-value args
        :rtype: ContractCall
        """
        if args:
            if len(args) == 1:
                (data, is_single) = (args[0], True)
            else:
                (data, is_single) = (list(args), False)
        elif kwargs:
            (data, is_single) = (kwargs, False)
        else:
            (data, is_single) = ([], False)

        if self.name:
            data = {self.name: data} if data or is_single else self.name

        parameters = self.script.parameter.encode(data)
        return ContractCall(
            parameters=parameters,
            address=self.address,
            script=self.script,
            shell=self.shell,
            key=self.key,
        )
