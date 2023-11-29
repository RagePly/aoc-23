from typing import Union, Callable, Tuple, Iterator, Any, cast, TypeGuard

from itertools import repeat
from operator import add, mul, sub, truediv, eq, floordiv

from functools import cache

def _isiter(x) -> TypeGuard[Iterator]:
    try:
        iter(x)
        return True
    except:
        return False

class vec:
    xs: Tuple[int]
    def __init__(self, *xs: Union[int, Iterator[int]]):
        if len(xs) == 1 and _isiter(xs[0]):
            self.xs = tuple(xs[0])
        else:
            self.xs = cast(Tuple[int], xs)
    def __repr__(self): return "vec(" + ", ".join(map(str, self.xs)) + ")"
    def __str__(self): return "(" + ", ".join(map(str, self.xs)) + ")"

    # list interface
    def __len__(self): return len(self.xs)
    def __getitem__(self, i: int | slice):
        if isinstance(i, int):
            return self.xs[i]
        return vec(*self.xs[i])

    def __getattr__(self, attr):
        if len(attr) == 1:
            try:
                return self["xyzw".index(attr)]
            except:
                pass
        else:
            return vec(*map(lambda x: getattr(self, x), attr))
        raise AttributeError(f"vec has no attribute {attr}")
    
    def reverse(self): return vec(*reversed(self))

    # iterable interface
    def __iter__(self): return iter(self.xs)
    def similar(self, v: Any): return vec(repeat(v, len(self)))
    def zipm(self, op: Callable[[int, int], int], other: Union["vec", int], reintrse: bool = False):
        if not isinstance(other, vec):
            other = self.similar(other)
        if not len(self) == len(other):
            raise ValueError(
                "can't zip vectors of different length")
        _op = op
        if reintrse:
            _op = lambda x, y: op(y, x)

        return vec(map(_op, self, other))

    # operator interface
    def __add__(self, other: Union["vec", int]): return self.zipm(add, other)
    def __sub__(self, other: Union["vec", int]): return self.zipm(sub, other)
    def __mul__(self, other: Union["vec", int]): return self.zipm(mul, other)
    def __floordiv__(self, other: Union["vec", int]): return self.zipm(floordiv, other)
    def __truediv__(self, other: Union["vec", int]): return self.zipm(truediv, other)

    def __radd__(self, other: Union["vec", int]): return self.zipm(add, other, True)
    def __rsub__(self, other: Union["vec", int]): return self.zipm(sub, other, True)
    def __rmul__(self, other: Union["vec", int]): return self.zipm(mul, other, True)
    def __rfloordiv__(self, other: Union["vec", int]): return self.zipm(floordiv, other, True)
    def __rtruediv__(self, other: Union["vec", int]): return self.zipm(truediv, other, True)

    def __eq__(self, other: "vec"): return self.xs == other.xs

    # vector interface
    def dot(self, other: Union["vec", int]) -> int: return sum(self.zipm(mul, other))
    def manhattan(self) -> int: return sum(map(lambda i: abs(i), self)) # map(abs, self) does not pass typecheck

    def dist(self, other: "vec"): return (other - self).manhattan()
    
    @staticmethod
    @cache
    def cardinal(n):
        return [vec((k if i == j else 0 for i in range(n))) for j in range(n) for k in [-1, 1]]
    
    @staticmethod
    def manhattan_betweeen(u: "vec", v: "vec"):
        return u.dist(v)

    def __hash__(self): return hash(self.xs)


