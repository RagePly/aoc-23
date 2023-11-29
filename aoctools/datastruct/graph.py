from typing import Dict, Any, List, Iterator, Tuple
from abc import ABC
from .vec import vec

class Graph(ABC):
    def children(self, node) -> Iterator[Tuple[Any, Any]]: ...
    def __contains__(self, node):
        try:
            next(self.children(node))
            return True
        except:
            return False

class graph(Graph):
    _nodes: Dict[Any, Dict[Any, int]]
    def __init__(self):
        self._nodes = {}
    def connect(self, a, b, weight=1):
        """Create edge a<->b with weight (defualt 1)"""
        self.point(a, b, weight)
        self.point(b, a, weight)
    def point(self, a, b, weight=1):
        """Create edge a->b with weight (default 1)"""
        self._nodes[a] = self._nodes.get(a, dict()) | {b: weight}
    def edges(self):
        """Return all edges in the graph, in arbitrary order"""
        return ((n, m, w) for n, e in self._nodes.items() for m, w in e.items())

    def nodes(self):
        """Return all nodes in the graph as a set"""
        nodes = set()
        for n, m, _ in self.edges():
            nodes.add(n)
            nodes.add(m)
        return nodes

    def children(self, node):
        """Return all children of a node"""
        return self._nodes.get(node, {}).items()

    def dftraverse(self, node, _visited=None):
        """Depth first traversal, does not take into consideration the cost of each node"""
        visited = _visited if _visited is not None else set()
        visited.add(node)
        for child, w in self.children(node):
            if child in visited: continue
            for subnode in self.dftraverse(child, visited):
                yield subnode
            yield node, child, w

    def bftraverse(self, node, _visited=None):
        """Breadth first traversal, does not take into consideration the cost of each node"""
        visited = _visited if _visited is not None else set()
        visited.add(node)
        children = []
        for child, w in self.children(node):
            if child in visited: continue
            yield node, child, w
            children.append(child)
        for child in children:
            for subnode in self.bftraverse(child, visited):
                yield subnode

class fgraph(Graph):
    """A functional graph-interface"""
    def __init__(self, childf):
        self._childf = childf
    def children(self, node):
        return self._childf(node)

class gridgraph(Graph):
    """A grid-graph. Nodes are coordinates"""
    def __init__(self, grid: List[List[bool]]):
        self._grid = grid
        self._height = len(grid)
        self._width = max(len(r) for r in grid)
    def __getitem__(self, coord: vec):
        if 0 <= coord.x < self._width and 0 <= coord.y < self._height:
            return self._grid[coord.y][coord.x]
        return False
    def children(self, coord: vec):
        up = coord + vec(0, -1), 1
        down = coord + vec(0, 1), 1
        left = coord + vec(-1, 0), 1
        right = coord + vec(1, 0), 1
        return filter(lambda c: self[c[0]], [up, down, left, right])
