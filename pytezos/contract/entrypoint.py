from pprint import pformat
from typing import Optional

from pytezos.contract.call import ContractCall
from pytezos.context.mixin import ContextMixin, ExecutionContext
from pytezos.michelson.sections.parameter import ParameterSection
from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.jupyter import get_class_docstring


class ContractEntrypoint(ContextMixin):
    """ Proxy class for spawning ContractCall instances.
    """

    def __init__(self, context: ExecutionContext, entrypoint: str):
        super(ContractEntrypoint, self).__init__(context=context)
        self.entrypoint = entrypoint

    def __repr__(self):
        res = [
            super(ContractEntrypoint, self).__repr__(),
            f'.entrypoint  # {self.entrypoint}',
            f'\nBuiltin\n(*args, **kwargs)  # build transaction parameters (see typedef)',
            f'\nTypedef\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
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

        return ContractCall(context=self.context,
                            parameters=self.encode(py_obj, self.context.mode))

    def decode(self, value, entrypoint: Optional[str] = None) -> dict:
        """ Convert from Michelson to Python type system

        :param value: Micheline JSON expression or Michelson value
        :param entrypoint: overwrite current entrypoint (in case you want to parse tx parameters)
        :return: Python object {entrypoint: value}
        """
        if isinstance(value, str):
            value = michelson_to_micheline(value)
        if entrypoint is None:
            entrypoint = self.entrypoint
        param_ty = ParameterSection.match(self.context.parameter_expr)
        parameters = {'entrypoint': entrypoint, 'value': value}
        py_obj = param_ty.from_parameters(parameters).to_python_object()
        return py_obj

    def encode(self, py_obj, mode: Optional[str] = None) -> dict:
        """ Encode transaction parameters from the given Python object

        :param py_obj: Python object
        :param mode: whether to use `readable` or `optimized` (or `legacy_optimized`) encoding
        :return: {entrypoint, value}
        """
        try:
            param_ty = ParameterSection.match(self.context.parameter_expr)
            return param_ty.from_python_object({self.entrypoint: py_obj}) \
                .to_parameters(mode=mode or self.context.mode)
        except MichelsonRuntimeError as e:
            print(self.__doc__)
            raise ValueError(f'Unexpected arguments: {pformat(py_obj)}', *e.args)
