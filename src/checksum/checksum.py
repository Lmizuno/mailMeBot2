import hashlib
import json


def checksumList(list):
    m = hashlib.md5()
    m.update(json.dumps(list).encode())
    return m.hexdigest()


def checksumString(str):
    m = hashlib.md5()
    m.update(str.encode())
    return m.hexdigest()
