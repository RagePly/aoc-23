from dataclasses import dataclass
from typing import Optional, List
from itertools import product

@dataclass
class line:
    a: int
    b: int
    def is_valid(self) -> bool: return self.a <= self.b
    def make_valid(self) -> "line":
        return line(self.a, self.b) if self.is_valid() else line(self.b, self.a)
    def intersection(self, other: "line") -> Optional["line"]:
        l = line(max(self.a, other.a), min(self.b, other.b))
        return l if l.is_valid() else None
    def copy(self) -> "line":
        return line(self.a, self.b)

@dataclass
class Box:
    h: line
    v: line

    def is_valid(self) -> bool: 
        return (
            self.h is not None and 
            self.v is not None and
            self.h.is_valid() and 
            self.v.is_valid())
    def intersection(self, other: "Box") -> Optional["Box"]:
        b = Box(self.h.intersection(other.h), self.v.intersection(other.v))
        return b if b.is_valid() else None
    def copy(self): return Box(self.h.copy(), self.v.copy())
    def cut(self, other: "Box") -> List["Box"]:
        bi = self.intersection(other)
        if bi is None: return [other.copy()]

        hs = [line(other.h.a, bi.h.a-1), bi.h.copy(), line(bi.h.b+1, other.h.b)]
        vs = [line(other.v.a, bi.v.a-1), bi.v.copy(), line(bi.v.b+1, other.v.b)]
        bs = map(lambda x: Box(*x), product(hs, vs))
        return [b for i, b in enumerate(bs) if i != 4 and b.is_valid()]

def box(l, r, t, b): return Box(line(l, r), line(t, b))