from ipykernel.kernelapp import IPKernelApp  # type: ignore

from michelson_kernel.kernel import MichelsonKernel

IPKernelApp.launch_instance(kernel_class=MichelsonKernel)
