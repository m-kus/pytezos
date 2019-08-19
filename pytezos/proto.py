import io
import os
import tarfile
import netstruct
import requests
import simplejson as json
from tqdm import tqdm
from binascii import hexlify
from collections import OrderedDict
from tempfile import TemporaryDirectory
from typing import List, Tuple

from pytezos.crypto import blake2b_32
from pytezos.encoding import base58_encode
from pytezos.tools.diff import make_patch, apply_patch, generate_unidiff_html
from pytezos.tools.docstring import get_class_docstring, InlineDocstring


def dir_to_files(path) -> List[Tuple[str, str]]:
    files = list()

    with open(os.path.join(path, 'TEZOS_PROTOCOL')) as f:
        index = json.load(f)

    for module in index['modules']:
        for ext in ['mli', 'ml']:
            name = f'{module.lower()}.{ext}'

            filename = os.path.join(path, name)
            if not os.path.exists(filename):
                continue

            with open(filename, 'r') as file:
                text = file.read()
                files.append((name, text))

    return files


def tar_to_files(path=None, raw=None) -> List[Tuple[str, str]]:
    assert path or raw

    fileobj = io.BytesIO(raw) if raw else None
    with tarfile.open(name=path, fileobj=fileobj) as tar:
        with TemporaryDirectory() as tmp_dir:
            tar.extractall(tmp_dir)
            files = dir_to_files(tmp_dir)

    return files


def url_to_files(url) -> List[Tuple[str, str]]:
    res = requests.get(url, stream=True)
    raw = b''

    for data in tqdm(res.iter_content()):
        raw += data

    return tar_to_files(raw=raw)


def files_to_proto(files: List[Tuple[str, str]]) -> dict:
    components = OrderedDict()

    for filename, text in files:
        name, ext = filename.split('.')
        key = {'mli': 'interface', 'ml': 'implementation'}[ext]
        name = name.capitalize()
        data = hexlify(text.encode()).decode()

        if name in components:
            components[name][key] = data
        else:
            components[name] = {'name': name, key: data}

    proto = {
        'expected_env_version': 0,  # TODO: this is V1
        'components': list(components.values())
    }
    return proto


def files_to_tar(files: List[Tuple[str, str]], output_path=None):
    fileobj = io.BytesIO() if output_path is None else None
    nameparts = os.path.basename(output_path).split('.')
    mode = 'w'
    if len(nameparts) == 3:
        mode = f'w:{nameparts[-1]}'

    with tarfile.open(name=output_path, fileobj=fileobj, mode=mode) as tar:
        for filename, text in files:
            file = io.BytesIO(text.encode())
            ti = tarfile.TarInfo(filename)
            ti.size = len(file.getvalue())
            tar.addfile(ti, file)

    if fileobj:
        return fileobj.getvalue()


def proto_to_files(proto: dict) -> List[Tuple[str, str]]:
    files = list()
    extensions = {'interface': 'mli', 'implementation': 'ml'}

    for component in proto.get('components', []):
        for key, ext in extensions.items():
            if key in component:
                filename = f'{component["name"].lower()}.{ext}'
                text = bytes.fromhex(component[key]).decode()
                files.append((filename, text))

    return files


def proto_to_bytes(proto: dict) -> bytes:
    res = b''

    for component in proto.get('components', []):
        res += netstruct.pack(b'I$', component['name'].encode())

        if component.get('interface'):
            res += b'\xff' + netstruct.pack(b'I$', bytes.fromhex(component['interface']))
        else:
            res += b'\x00'

        # we should also handle patch case
        res += netstruct.pack(b'I$', bytes.fromhex(component.get('implementation', '')))

    res = netstruct.pack(b'hI$', proto['expected_env_version'], res)
    return res


class Proto(metaclass=InlineDocstring):

    def __init__(self, proto):
        self._proto = proto

    def __repr__(self):
        res = [
            super(Proto, self).__repr__(),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def __iter__(self):
        return iter(proto_to_files(self._proto))

    @classmethod
    def from_uri(cls, uri):
        """
        Loads protocol implementation from various sources and converts it to the RPC-like format
        :param uri: link/path to a tar archive or path to a folder with extracted contents
        :return: Protocol instance
        """
        if uri.startswith('http'):
            files = url_to_files(uri)
        elif os.path.exists(os.path.expanduser(uri)):
            files = tar_to_files(uri)
        elif os.path.isdir(uri):
            files = dir_to_files(uri)
        else:
            raise ValueError(uri)

        return Proto(files_to_proto(files))

    def index(self) -> dict:
        """
        Generates TEZOS_PROTOCOL file
        :return: dict with protocol hash and modules
        """
        data = {
            'hash': self.hash(),
            'modules': list(map(lambda x: x['name'], self._proto.get('components', [])))
        }
        return data

    def export_tar(self, output_path=None):
        """
        Creates a tarball and dumps to a file or returns bytes
        :param output_path: Path to the tarball [optional]. You can add .bz2 or .gz extension to make it compressed
        :return: bytes if path is None or nothing
        """
        files = proto_to_files(self._proto)
        files.append(('TEZOS_PROTOCOL', json.dumps(self.index())))
        return files_to_tar(files, output_path)

    def export_html(self, output_path=None):
        """
        Generates github-like side-by-side diff viewe, powered by diff2html.js
        :param output_path: will write to this file if specified
        :return: html string if path is not specified
        """
        diffs = [text for filename, text in self if text]
        return generate_unidiff_html(diffs, output_path=output_path)

    def diff(self, proto, context_size=3):
        """
        Calculates file diff between two protocol versions
        :param proto: an instance of Protocol
        :param context_size: number of context lines before and after the change
        :return: patch in proto format
        """
        files = list()
        yours = dict(iter(self))
        theirs = proto_to_files(proto())

        for filename, their_text in theirs:
            patch = make_patch(
                a=yours.get(filename, ''),
                b=their_text,
                filename=filename,
                context_size=context_size
            )
            files.append((filename, patch))

        return Proto(files_to_proto(files))

    def patch(self, patch):
        """
        Applies unified diff and returns full-fledged protocol
        :param patch: an instance of Protocol containing diff of files
        :return: Protocol instance
        """
        files = list()
        yours = dict(iter(self))
        diff = proto_to_files(patch())

        for filename, diff_text in diff:
            text = yours.get(filename, '')
            if diff_text:
                text = apply_patch(text, diff_text)
            files.append((filename, text))

        return Proto(files_to_proto(files))

    def hash(self):
        hash_digest = blake2b_32(proto_to_bytes(self._proto)).digest()
        return base58_encode(hash_digest, b'P').decode()
