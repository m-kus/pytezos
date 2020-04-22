import json
import re
import os

tests_dir = os.path.dirname(__file__)


def abspath(path):
    return os.path.join(tests_dir, path)


def relpath(path):
    return os.path.relpath(path, start=tests_dir)


def get_data(path, strip=True):
    with open(os.path.join(tests_dir, path)) as f:
        data = f.read()
    if path.endswith('.json'):
        return json.loads(data)
    elif path.endswith('.tz'):
        if strip:
            data = re.sub(r'\n\s*', ' ', data)
            data = data.replace('{  }', '{}')
        return data
    elif path.endswith('.hex'):
        return bytes.fromhex(data)
    else:
        assert False, path
