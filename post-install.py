import json
import os
import shutil
import sys
from os.path import join, dirname

from jupyter_client.kernelspec import KernelSpecManager
from tempfile import TemporaryDirectory

kernel_json = {
    "argv": [sys.executable, "-m", "michelson_kernel", "-f", "{connection_file}"],
    "display_name": "Michelson",
    "language": "michelson",
    "codemirror_mode": "michelson"
}
kernel_js_path = join(dirname(__file__), 'src', 'michelson_kernel', 'kernel.js')

kernel_spec = KernelSpecManager()

with TemporaryDirectory() as td:
    # NOTE: Starts off as 700, not user readable
    os.chmod(td, 0o755)
    shutil.copy(kernel_js_path, join(td, 'kernel.js'))
    with open(os.path.join(td, 'kernel.json'), 'w') as f:
        json.dump(kernel_json, f, sort_keys=True)

    kernel_spec.install_kernel_spec(td, 'michelson', prefix=sys.prefix)
