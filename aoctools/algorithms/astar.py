from math import inf
from ..datastruct.graph import Graph
from .pqueue import pqueue

def A_star(nodes: Graph, start, end, heuristic=None):
    h = heuristic if heuristic is not None else lambda x, y: 0
    queue = pqueue()
    queue.insert(start, h(start, end))
    gscore = { start: 0 }
    path = {}

    while not queue.is_empty():
        next_node, fscore = queue.next()
        ngscore = gscore[next_node]
        if next_node == end: break

        for child, w in nodes.children(next_node):
            score = ngscore + w
            if score < gscore.get(child, inf):
                path[child] = next_node
                gscore[child] = score
                queue.change(child, score + h(child, end))
    else: # if end not found
        return None

    # backtrack
    backtrack = [end]
    while (next_node := path.get(backtrack[-1])) is not None:
        backtrack.append(next_node)
    backtrack.reverse()
    return backtrack, gscore[end]

