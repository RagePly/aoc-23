from collections import defaultdict
from heapq import heappop, heappush
def rpath(cf, e, s):
    p = []
    n = cf[e][0]
    while n != s:
        p.append(n)
        n = cf[n][0]
    return p
        
def part1(src):
    g = defaultdict(set)
    for line in src.splitlines():
        c, cs = line.split(": ")
        for cp in cs.split():
            g[c].add(cp)
            g[cp].add(c)
    g = {k:list(v) for k,v in g.items()}
    
    found = defaultdict(int)
    nodes = list(g.keys())
    count = 0
    start = nodes[0] 
    for end in nodes[1:len(nodes)//2]:
        potential = set()
        paths = []
        while len(paths) < 4:
            camefrom = {}
            visited = set()
            queue = [(0,0,start)]
            while queue:
                d, _, n = heappop(queue)

                if n == end:
                    break
                if n in visited:
                    continue
                visited.add(n)
                
                for c in g[n]:
                    if c in potential: 
                        continue
                    if camefrom.get(c, (None, 10000000))[1] > d+1:
                        camefrom[c] = (n, d+1)
                    count += 1
                    heappush(queue, (d+1, count, c))
            else:
                break
            
            path = rpath(camefrom, end, start)
            paths.append(path)
            potential |= set(path)
        else:
            continue
                    
        if len(paths) == 3:
            for p in paths:
                for ii in range(len(p)-1):
                    pot = tuple(sorted(p[ii:ii+2]))
                    found[pot] += 1

    stats = list(sorted(found.items(), key=lambda f: f[1], reverse=True))
    top = stats[0][1]
    usable = list(filter(lambda f: f[1] > top // 2, stats))

    for i in range(len(usable)-2):
        for j in range(i+1,len(usable)-1):
            for k in range(j+1,len(usable)):
                gt = {n:list(cs) for n,cs in g.items()}
                for (n1,n2), _ in [usable[i], usable[j], usable[k]]:
                    gt[n1].remove(n2)
                    gt[n2].remove(n1)
                v = set()
                q = [n1]
                while q:
                    n = q.pop()
                    if n in v: continue
                    v.add(n)
                    if n == n2: break
                    for c in gt[n]:
                        q.append(c)
                else:
                    return (len(g) - len(v)) * len(v)
