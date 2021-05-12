from typing import Any, Dict, List

from pytezos.context.impl import ExecutionContext  # type: ignore
from pytezos.michelson.program import MichelsonProgram
from pytezos.operation.result import OperationResult


class ContractCallResult(OperationResult):
    """Encapsulates the result of a contract invocation."""

    @classmethod
    def from_run_operation(cls, operation_group: Dict[str, Any], context: ExecutionContext) -> List['ContractCallResult']:
        """Get a list of results from an operation group content with metadata.

        :param operation_group: {..., "contents": [{..., kind: "transaction", ...}]}
        :param context: execution context
        :rtype: ContractCallResult
        """
        results: List['OperationResult'] = list()
        for content in OperationResult.iter_contents(operation_group):
            if content['kind'] == 'transaction':
                if content['destination'] == context.address:
                    results.append(cls.from_transaction(content))
            elif content['kind'] == 'origination':
                result = cls.get_result(content)
                if context.address in result.get('originated_contracts', []):
                    results.append(cls.from_origination(content))

        program = MichelsonProgram.load(context)

        def decode_result(res: OperationResult) -> 'ContractCallResult':
            kwargs = {}  # type: ignore
            if hasattr(res, 'storage') and res.storage is not None:  # type: ignore
                storage = program.storage.from_micheline_value(res.storage)  # type: ignore
                if hasattr(res, 'lazy_diff'):
                    kwargs.update(lazy_diff=res.lazy_diff)  # type: ignore
                    storage = storage.merge_lazy_diff(res.lazy_diff)  # type: ignore
                kwargs.update(storage=storage.to_python_object())
            if hasattr(res, 'parameters'):
                parameters = program.parameter.from_parameters(res.parameters)  # type: ignore
                kwargs.update(parameters=parameters)
            if hasattr(res, 'operations'):
                kwargs.update(operations=res.operations)  # type: ignore
            return cls(**kwargs)

        return list(map(decode_result, results))

    @classmethod
    def from_run_code(cls, response: Dict[str, Any], parameters, context: ExecutionContext) -> 'ContractCallResult':
        """Parse a result of :py:meth:`pytezos.contract.call.ContractCall.run_code` execution.

        :param response: RPC response (JSON)
        :param parameters: {"entrypoint": str, "value": $Micheline}
        :param context: execution context
        :rtype: ContractCallResult
        """
        program = MichelsonProgram.load(context)
        parameters = program.parameter.from_parameters(parameters)
        storage = program.storage.from_micheline_value(response['storage'])
        extended_storage = storage.merge_lazy_diff(response.get('lazy_diff', []))
        return cls(
            parameters=parameters.to_python_object(),
            storage=extended_storage.to_python_object(lazy_diff=True),
            lazy_diff=response.get('lazy_diff', []),
            operations=response.get('operations', []),
        )
