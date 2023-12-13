import re
import functools
import contextlib

def default(value, _default):
    return value if value is not None else _default

def _partition_re(pattern, text):
    i = 0
    for m in re.finditer(pattern, text):
        yield text[i:m.start()]
        yield m[0]
        i = m.end()    
    yield text[i:]


@functools.cache
def partition(pattern, text):
    if not isinstance(pattern, re.Pattern):
        pattern = re.compile(str(pattern))
    return list(_partition_re(pattern, text))

def partition_map(f, pattern, text):
    for i, x in enumerate(partition(pattern, text)):
        if i % 2 == 0:
            yield x
        else:
            yield f(x)

def unzip(it,w=2):
    parts = tuple([] for _ in range(w))
    for tup in it:
        for i in range(len(parts)):
            parts[i].append(tup[i])
    return parts

class _AbandonException(Exception):
    def __init__(self, i):
        super().__init__("Tried to abandon execution without a context")
        self._i = i
class _AbandonHandle:
    def abandon(self):
        raise _AbandonException(id(self))

@contextlib.contextmanager
def abandon():
    handle = _AbandonHandle()
    try:
        yield handle
    except _AbandonException as ae:
        if ae._i == id(handle):
            pass
        else:
            raise ae
