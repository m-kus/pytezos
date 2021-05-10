import json
import os
import shutil
import sys
from os.path import dirname, join
from tempfile import TemporaryDirectory

import click
from ipykernel.kernelapp import IPKernelApp  # type: ignore
from jupyter_client.kernelspec import KernelSpecManager  # type: ignore

from michelson_kernel import __version__
from michelson_kernel.kernel import MichelsonKernel


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli(*_args, **_kwargs):
    pass


@cli.command(help='Run Michelson kernel', context_settings={"ignore_unknown_options": True})
@click.argument('args', nargs=-1, type=str)
@click.pass_context
def run(_ctx, args) -> None:
    IPKernelApp.launch_instance(argv=args, kernel_class=MichelsonKernel)


@cli.command(help='Install Michelson kernel in current environment')
@click.pass_context
def install(_ctx) -> None:
    kernel_json = {
        "argv": [sys.executable, "-m", "michelson_kernel", "run", "-f", "{connection_file}"],
        "display_name": "Michelson",
        "language": "michelson",
        "codemirror_mode": "michelson",
    }
    kernel_js_path = join(dirname(__file__), 'kernel.js')

    kernel_spec = KernelSpecManager()

    with TemporaryDirectory() as td:
        # NOTE: Starts off as 700, not user readable
        os.chmod(td, 0o755)
        shutil.copy(kernel_js_path, join(td, 'kernel.js'))
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)

        kernel_spec.install_kernel_spec(td, 'michelson', prefix=sys.prefix)


@cli.command(help='Remove Michelson kernel from current environment')
@click.pass_context
def remove(_ctx) -> None:
    kernel_spec = KernelSpecManager()
    kernel_spec.remove_kernel_spec('michelson')
