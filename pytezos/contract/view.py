from pytezos.context.mixin import ContextMixin  # type: ignore


class ContractView(ContextMixin):

    def __call__(*args, **kwargs) -> ContractCall:
        # NOTE: given the off-chain view contract parameter type `pair <view-parameter-type> <target-contract-storage-type>`
        # this method accepts ONLY the view parameters, and queries current storage of the target contract internally
        raise NotImplementedError
