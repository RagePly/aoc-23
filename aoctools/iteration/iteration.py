class _StopIteration: ...
def merge(x, y, pred=None):
    """Merge two iterators using predicate that 
    returns true if item should be taken from x, false otherwise"""
    x = iter(x)
    y = iter(y)
    nx = next(x, _StopIteration)
    ny = next(y, _StopIteration)
    pred = pred if pred is not None else lambda x, _y: x is not None
    
    while True:
        if nx == _StopIteration and ny == _StopIteration:
            break

        if nx == _StopIteration:
            yield ny
            ny = next(y, _StopIteration)
        elif ny == _StopIteration:
            yield nx
            nx = next(x, _StopIteration)
        elif pred(nx, ny):
            yield nx
            nx = next(x, _StopIteration)
        else:
            yield ny
            ny = next(y, _StopIteration)

def insert(x, y):
    x = iter(x)
    y = iter(y)
    nx = next(x, _StopIteration)
    ny = next(y, _StopIteration)
    
    while True:
        if nx == _StopIteration and ny == _StopIteration:
            break

        if nx == _StopIteration:
            yield ny
            ny = next(y, _StopIteration)
        elif ny == _StopIteration:
            if nx is None:
                raise RuntimeError(
                    "insertion point could not be filled because element pool is exhausted")
            yield nx
            nx = next(x, _StopIteration)
        elif nx is not None:
            yield nx
            nx = next(x, _StopIteration)
        else:
            yield ny
            ny = next(y, _StopIteration)
            nx = next(x, _StopIteration)

def lenlist(iterable): return len(list(iterable))