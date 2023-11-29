from itertools import islice
from .iteration import merge, insert

def blocks(l, n):
    it = iter(l)
    while (e := list(islice(it, n))):
        yield e

__all__ = [
    'merge',
    'insert',
    'blocks'
]