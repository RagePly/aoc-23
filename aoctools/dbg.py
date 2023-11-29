from .util import default
from functools import wraps
_DEBUG_INFO = {}

def _indent(s):
    global _DEBUG_INFO
    lines = s.split('\n')
    lines = ["  " * _DEBUG_INFO['indentation'] + line for line in lines]
    return "\n".join(lines)

def _push_scope():
    global _DEBUG_INFO
    _DEBUG_INFO['indentation'] += 1
def _pop_scope():
    global _DEBUG_INFO
    _DEBUG_INFO['indentation'] -= 1

def set_dbg(is_on):
    global _DEBUG_INFO
    reset_dbg()
    _DEBUG_INFO['on'] = bool(is_on)

def reset_dbg():
    global _DEBUG_INFO
    _DEBUG_INFO = {
        'indentation': 0,
        'on': True
        }

def dbg(x, prompt=None):
    """log value to console"""
    global _DEBUG_INFO
    if _DEBUG_INFO['on']:
        prompt = default(prompt, '')
        print(_indent(prompt + repr(x)))
    return x

def dbgf(f):
    global _DEBUG_INFO
    @wraps(f) 
    def wrapper(*args, **kwargs):
        if _DEBUG_INFO['on']:
            print(_indent('entering ' + f.__name__ + ':'))
            _push_scope()
            temp = dbg(f(*args, **kwargs), 'return ')
            _pop_scope()
            print(_indent('end'))
            return temp
        return f(*args, **kwargs)
    return wrapper

set_dbg(False)

__all__ = [
    'set_dbg',
    'reset_dbg',
    'dbg',
    'dbgf'
]
