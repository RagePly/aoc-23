import re
import functools

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
