from heapq import heappop, heappush
def part1(src):
    RIGHT,UP,LEFT,DOWN = 0,1,2,3 
    arrows = ">^<v"
    grid = list(map(list, src.splitlines()))
    h,w = len(grid), len(grid[0])
    start = 1, 0
    end = w-2, h-1
    
    steps = 0
    queue = [(0, steps, DOWN, start, set())]
    dists = []

    while queue:
        steps += 1
        dist, _, d, (x,y), visited = heappop(queue) 

        if (x,y) in visited:
            continue
        visited.add((x,y))

        if (x,y) == end:
            dists.append(dist)
            continue

        for nd, (dx,dy) in enumerate([(1,0), (0,-1), (-1,0), (0,1)]):
            nx,ny = x+dx, y+dy 
            if nd == (d+2) % 4: # backwards
                continue
            
            t = grid[ny][nx]
            if t == "#":
                continue
            elif t == ".":
                heappush(queue, (dist+1, steps, nd, (nx,ny), set(visited)))
            elif arrows.index(t) == nd:
                heappush(queue, (dist+1, steps, nd, (nx,ny), set(visited)))

    return max(dists)

from collections import defaultdict
from bisect import insort
def part2(src):
    grid = list(map(list, src.splitlines()))
    h,w = len(grid), len(grid[0])
    start = 1, 0
    end = w-2, h-1

    nodes = set([start,end])
    for y in range(1, h-1):
        for x in range(1, w-1):
            paths = 0
            t = grid[y][x]
            if t == '#': continue
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x+dx,y+dy
                t = grid[ny][nx]
                if t != '#':
                    paths+=1
            if paths > 2:
                nodes.add((x,y))

    graph = defaultdict(dict)
    for node in nodes:
        steps = 0
        queue = [(0, steps, node)]
        visited = set()
        while queue:
            dist, _, (x,y) = heappop(queue) 

            if (x,y) in visited:
                continue
            visited.add((x,y))

            if (x,y) != node and (x,y) in nodes:
                graph[node][x,y] = dist
                continue

            for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
                nx,ny = x+dx, y+dy 
                if nx < 0 or nx >= w or ny < 0 or ny >= h: continue
                t = grid[ny][nx]
                if t == "#": continue
                steps += 1
                heappush(queue, (dist+1, steps, (nx,ny)))
    
    # g = Graph("hello", engine="sfdp")
    # v = set()
    # for n,cs in graph.items():
    #     for c,d in cs.items():
    #         if c not in v:
    #             g.edge(str(n), str(c), label=str(d))
    #     v.add(n)
    # g.render()

    queue = [(0, start, set())]
    m = 0
    while queue:
        d, node, visited = queue.pop()

        if node in visited:
            continue
        if node == end:
            m = max(m, d)
        visited.add(node)
        
        for c,nd in graph[node].items():
            queue.append((d+nd,c,set(visited)))

    return m
