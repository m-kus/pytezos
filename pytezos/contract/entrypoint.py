from pytezos.contract.call import ContractCall
from pytezos.context.mixin import ContextMixin, ExecutionContext
from pytezos.michelson.sections.parameter import ParameterSection


class ContractEntrypoint(ContextMixin):
    """ Proxy class for spawning ContractCall instances.
    """

    def __init__(self, context: ExecutionContext, entrypoint: str):
        super(ContractEntrypoint, self).__init__(context=context)
        self.entrypoint = entrypoint

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
                py_obj = args[0]
            else:
                py_obj = args
        elif kwargs:
            py_obj = kwargs
        else:
            py_obj = None

        param_ty = ParameterSection.match(self.context.parameter_expr)
        parameters = param_ty.from_python_object({self.entrypoint: py_obj}).to_micheline_value()
        return ContractCall(context=self.context, parameters=parameters)
