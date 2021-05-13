import functools
import operator
from typing import Any, Dict, Iterator, List

from pytezos.rpc.errors import RpcError


class OperationResult:
    """Operation result representation + useful parsing helpers for operation group"""

    def __init__(self, **props):
        self.props = props
        for key, value in props.items():
            setattr(self, key, value)

    def __repr__(self):
        res = [
            super(OperationResult, self).__repr__(),
            '\nProperties',
            *list(map(lambda x: f'.{x}', self.props)),
        ]
        return '\n'.join(res)

    @staticmethod
    def iter_contents(operation_group: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
        """ Lazily iterate operation group contents including internal operations.

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        :returns: generator
        """
        contents = operation_group.get('contents', [operation_group])
        for content in contents:
            yield {'internal': False, **content}
            internal_operation_results = content.get('metadata', {}).get('internal_operation_results', [])
            for result in internal_operation_results:
                yield {'internal': True, **result}

    @staticmethod
    def iter_results(operation_group: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
        """ Lazily iterate operation results including internal operation results.

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        :returns: generator
        """
        for content in OperationResult.iter_contents(operation_group):
            if content['internal'] and content.get('result'):
                yield content['result']
            elif not content['internal'] and content.get('metadata', {}).get('operation_result'):
                yield content['metadata']['operation_result']

    @staticmethod
    def consumed_gas(operation_group: Dict[str, Any]) -> int:
        """ Get total consumed gas for an operation group (recursively).

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        """
        return sum(
            map(
                lambda x: int(x.get('consumed_gas', '0')),
                OperationResult.iter_results(operation_group),
            ),
        )

    @staticmethod
    def paid_storage_size_diff(operation_group: Dict[str, Any]) -> int:
        """ Get total paid storage size diff for an operation group (recursively).

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        """
        return sum(
            map(
                lambda x: int(x.get('paid_storage_size_diff', '0')),
                OperationResult.iter_results(operation_group),
            ),
        )

    @staticmethod
    def burned(operation_group: Dict[str, Any]) -> int:
        """ Get total burned (due to account allocations) for an operation group (recursively).

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        """
        return sum(
            map(
                lambda x: 257 if x.get('allocated_destination_contract') or x.get('originated_contracts') else 0,
                OperationResult.iter_results(operation_group),
            )
        )

    @staticmethod
    def is_applied(operation_group: Dict[str, Any]) -> bool:
        """ Check if ALL operations in a group are applied.

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        """
        return all(map(lambda x: x['status'] == 'applied', OperationResult.iter_results(operation_group)))

    @staticmethod
    def errors(operation_group: Dict[str, Any]) -> List[Dict[str, Any]]:
        """ Collect errors from all operation results in a group.

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        :returns: list of errors [{"id": "", ...}]
        """
        all_errors = (
            result.get("errors", []) if result["status"] != "applied" else [] for result in OperationResult.iter_results(operation_group)
        )
        return functools.reduce(operator.iconcat, all_errors, [])

    @staticmethod
    def originated_contracts(operation_group: Dict[str, Any]) -> List[str]:
        """ Collect originated contract addresses from all operation results in a group.

        :param operation_group: {"branch": "B...", "contents": [...], ...} \
        OR a single content {"kind": "transaction", ...}
        :returns: list of addresses ["tz12345...", ...]
        """
        originated_contracts = list()
        for result in OperationResult.iter_results(operation_group):
            originated_contracts.extend(result.get('originated_contracts', []))
        return originated_contracts

    @staticmethod
    def get_contents(operation_group: Dict[str, Any], **predicates) -> List[Dict[str, Any]]:
        def match(x):
            return all(map(lambda pred: x.get(pred[0]) == pred[1], predicates.items()))

        if not predicates:
            return operation_group['contents']
        else:
            return list(filter(match, OperationResult.iter_contents(operation_group)))

    @staticmethod
    def get_result(content: Dict[str, Any]) -> Dict[str, Any]:
        if content.get('metadata'):
            return content['metadata']['operation_result']
        elif content.get('result'):
            return content['result']
        else:
            assert False, content

    @classmethod
    def from_operation_group(cls, operation_group: Dict[str, Any], **predicates) -> List['OperationResult']:
        """ Initialize with operation group contents.

        :param operation_group: operation_group: {"branch": "B...", "contents": [...], ...} \
        :param predicates: filter contents using predicates `field=value`
        :rtype: List[OperationResult]
        """
        if not cls.is_applied(operation_group):
            raise RpcError.from_errors(cls.errors(operation_group))

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
    def from_origination(cls, content: Dict[str, Any]) -> 'OperationResult':
        """Initialize with origination content.

        :param content:
        :rtype: OperationResult
        """
        operation_result = cls.get_result(content)
        return cls(
            storage=content['script']['storage'],
            originated_contracts=operation_result['originated_contracts'],
        )

    @classmethod
    def from_transaction(cls, content: Dict[str, Any]) -> 'OperationResult':
        """Initialize with transaction content.

        :param content:
        :rtype: OperationResult
        """
        operation_result = cls.get_result(content)
        return cls(
            parameters=content.get('parameters'),
            storage=operation_result.get('storage'),
            lazy_diff=operation_result.get('lazy_diff', []),
            # TODO: if it is already an internal operation, we should think... (build a tree?)
            operations=cls.get_contents(content, source=content['destination']),
        )
