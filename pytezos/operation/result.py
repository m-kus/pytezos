import functools
import operator
from pytezos.rpc.errors import RpcError


class OperationResult:

    def __init__(self, **props):
        self.props = props
        for key, value in props.items():
            setattr(self, key, value)

    def __repr__(self):
        res = [
            super(OperationResult, self).__repr__(),
            '\nProperties',
            *list(map(lambda x: f'.{x}', self.props))
        ]
        return '\n'.join(res)

    @staticmethod
    def iter_contents(operation_group: dict):
        contents = operation_group.get('contents', [operation_group])
        for content in contents:
            yield {'internal': False, **content}
            internal_operation_results = content.get('metadata', {}).get('internal_operation_results', [])
            for result in internal_operation_results:
                yield {'internal': True, **result}

    @staticmethod
    def iter_results(operation_group: dict):
        for content in OperationResult.iter_contents(operation_group):
            if content['internal'] and content.get('result'):
                yield content['result']
            elif not content['internal'] and content.get('metadata', {}).get('operation_result'):
                yield content['metadata']['operation_result']

    @staticmethod
    def consumed_gas(operation_group):
        return sum(map(lambda x: int(x.get('consumed_gas', '0')),
                       OperationResult.iter_results(operation_group)))

    @staticmethod
    def paid_storage_size_diff(operation_group):
        return sum(map(lambda x: int(x.get('paid_storage_size_diff', '0')),
                       OperationResult.iter_results(operation_group)))

    @staticmethod
    def is_applied(operation_group):
        return all(map(lambda x: x['status'] == 'applied',
                       OperationResult.iter_results(operation_group)))

    @staticmethod
    def errors(operation_group: dict):
        all_errors = (
            result.get("errors", []) if result["status"] != "applied" else []
            for result in OperationResult.iter_results(operation_group)
        )
        return functools.reduce(operator.iconcat, all_errors, [])

    @staticmethod
    def originated_contracts(operation_group: dict):
        originated_contracts = list()
        for result in OperationResult.iter_results(operation_group):
            originated_contracts.extend(result.get('originated_contracts', []))
        return originated_contracts

    @staticmethod
    def get_contents(operation_group: dict, **predicates):
        def match(x):
            return all(map(lambda pred: x.get(pred[0]) == pred[1], predicates.items()))

        if not predicates:
            assert len(operation_group['contents']) == 1
            return operation_group['contents']
        else:
            return list(filter(match, OperationResult.iter_contents(operation_group)))

    @staticmethod
    def get_result(content):
        if content.get('metadata'):
            return content['metadata']['operation_result']
        elif content.get('result'):
            return content['result']
        else:
            assert False, content

    @classmethod
    def from_operation_group(cls, operation_group: dict, **predicates):
        if not cls.is_applied(operation_group):
            raise RpcError.from_errors(cls.errors(operation_group)) from None

        def dispatch(content):
            if content['kind'] == 'transaction':
                return cls.from_transaction(content)
            elif content['kind'] == 'origination':
                return cls.from_origination(content)
            else:
                return content

        contents = cls.get_contents(operation_group, **predicates)
        return list(map(dispatch, contents))

    @classmethod
    def from_origination(cls, content: dict):
        operation_result = cls.get_result(content)
        return cls(
            storage=content['script']['storage'],
            originated_contracts=operation_result['originated_contracts']
        )

    @classmethod
    def from_transaction(cls, content: dict):
        operation_result = cls.get_result(content)
        return cls(
            parameters=content.get('parameters'),
            storage=operation_result.get('storage'),
            big_map_diff=operation_result.get('big_map_diff', []),
            # TODO: if it is already an internal operation, we should think... (build a tree?)
            operations=cls.get_contents(content, source=content['destination'])
        )
