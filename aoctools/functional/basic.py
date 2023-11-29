"""Simple functional utility patterns """
from ..iteration import insert

def echo(x):
    """Return x"""
    return x

def const(x):
    """Return function that ignores its' input and allways returns `x`"""
    return lambda *_x: x

def chain(*f):
    """Function composition. `chain(f,g,h)(x) == f(g(h(x)))`
    """
    functions = list(reversed(f))
    def _inner(x):
        res = x
        for func in functions:
            res = func(res)
        return res
    return _inner

def partial(f, *xs): 
    """Partial application. Returns `f` with some arguments filled in.
    ## Example
    ```py
        >>> from aoctools.functional import partial
        >>> from operator import mul
        >>> times10 = partial(mul, 10)
        >>> times10(12)
        120
        >>>
    ```"""
    return lambda *x: f(*xs, *x)

def pmap(f):
    """Partially apply function `f` to built-in-`map`"""
    return partial(map, f)

def flip(f):
    """Returns binary function `f` with its' arguments flipped: `f(x, y) -> f(y, x)`"""
    return lambda x, y: f(y, x)
def flip_all(f): 
    """Reverse the order of all arguments in `f`"""
    return lambda *xs: f(*reversed(xs))

def maybe(f, default, item):
    """Apply function `f` to item if it exists otherwise return the default value
    ## Example
    >>> from aoctools.functional import maybe
    >>> maybe(lambda x: f"was {x}", "was none", 123)
    'was 123'
    >>> maybe("lambda x: f"was {x}", was none", None) 
    'was none'
    """
    return default if item is None else f(item)

def mapm(f, m):
    "map-maybe"
    return f(m) if m is not None else None

def template(f, *xs):
    """Like `partial`, returns `f` with all non-`None` arguments filled in 
    ## Example
    ```py
        >>> from aoctools.functional import template
        >>> def foo(*xs): return " ".join(map(str, xs)) 
        ... 
        >>> t_foo = template(foo, 1, None, 2) # remaining arguments are treated as None
        >>> t_foo(3, 4)
        '1 3 2 4'
    ```
    """
    return lambda *ys: f(*insert(xs, ys))

def ifelse(t, i, e): 
    "if else in functional form"
    return i if t else e
