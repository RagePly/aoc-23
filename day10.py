from heapq import heappush, heappop
def part1(src):
    m = [[c for c in line] for line in src.splitlines()]
    p = [(x,y) for y in range(len(m)) for x in range(len(m[y])) if m[y][x] == 'S'][0]
    
    dmax = 0
    q = [(0,p,None)]
    visited = set()
    while q:
        d, this, prev = heappop(q)
        if this in visited: continue
        else: visited.add(this)

        if d > dmax: dmax = d
        
        x,y = this
        c = m[y][x] 

        if c == 'S':
            t = m[y-1][x]
            b = m[y+1][x]
            l = m[y][x-1]
            r = m[y][x+1]

            if t in ("|", "F", "7"):
                heappush(q, (d+1, (x,y-1), (x,y)))
            if b in ("|", "L", "J"):
                heappush(q, (d+1, (x,y+1), (x,y)))
            if l in ("-", "F", "L"):
                heappush(q, (d+1, (x-1,y), (x,y)))
            if r in ("-", "7", "J"):
                heappush(q, (d+1, (x+1,y), (x,y)))
            continue
        
        dx, dy = x-prev[0], y-prev[1]

        if c == "-":
            heappush(q, (d+1, (x+dx,y), (x,y)))
        elif c == "|":
            heappush(q, (d+1, (x,y+dy), (x,y)))
        elif c == "F":
            heappush(q, (d+1, (x+1,y) if dy == -1 else (x,y+1), (x,y)))
        elif c == "L":
            heappush(q, (d+1, (x+1,y) if dy == 1 else (x,y-1), (x,y)))
        elif c == "J":
            heappush(q, (d+1, (x-1,y) if dy == 1 else (x,y-1), (x,y)))
        elif c == "7":
            heappush(q, (d+1, (x-1,y) if dy == -1 else (x,y+1), (x,y)))
    return dmax
        


def part2(src):
    m = [[c for c in line] for line in src.splitlines()]
    p = [(x,y) for y in range(len(m)) for x in range(len(m[y])) if m[y][x] == 'S'][0]
    
    q = [(0,p,None)]
    visited = set()
    ts = [[None for x in range(len(m[0]))] for y in range(len(m))]
    while q:
        d, this, prev = heappop(q)
        if this in visited: continue
        else: visited.add(this)

        x,y = this
        c = m[y][x] 
        if c == 'S':
            t = m[y-1][x]
            b = m[y+1][x]
            l = m[y][x-1]
            r = m[y][x+1]

            if t in ("|", "F", "7"):
                heappush(q, (d+1, (x,y-1), (x,y)))
            elif b in ("|", "L", "J"):
                heappush(q, (d+1, (x,y+1), (x,y)))
            elif l in ("-", "F", "L"):
                heappush(q, (d+1, (x-1,y), (x,y)))
            elif r in ("-", "7", "J"):
                heappush(q, (d+1, (x+1,y), (x,y)))
            continue
        
        dx, dy = x-prev[0], y-prev[1]
        if c == "-":
            heappush(q, (d+1, (x+dx,y), (x,y)))
            rims = [(x,y-dx)] ,[(x,y+dx)]
        elif c == "|":
            heappush(q, (d+1, (x,y+dy), (x,y)))
            rims = [(x+dy,y)] ,[(x-dy,y)]
        elif c == "F":
            heappush(q, (d+1, (x+1,y) if dy == -1 else (x,y+1), (x,y)))
            r = [(x-1,y), (x-1,y-1), (x,y-1)]
            rims = (r,[]) if dy == -1 else ([],r)
        elif c == "L":
            heappush(q, (d+1, (x+1,y) if dy == 1 else (x,y-1), (x,y)))
            r = [(x-1,y), (x-1,y+1), (x,y+1)]
            rims = ([],r) if dy == 1 else (r,[])
        elif c == "J":
            heappush(q, (d+1, (x-1,y) if dy == 1 else (x,y-1), (x,y)))
            r = [(x+1,y), (x+1,y+1), (x,y+1)]
            rims = (r,[]) if dy == 1 else ([],r)
        elif c == "7":
            heappush(q, (d+1, (x-1,y) if dy == -1 else (x,y+1), (x,y)))
            r = [(x+1,y), (x+1,y-1), (x,y-1)]
            rims = ([],r) if dy == -1 else (r,[])

        for px,py in rims[0]:
            if px < 0 or py < 0: continue
            try:
                ts[py][px] = "lhs"
            except IndexError:
                pass
        for px,py in rims[1]:
            if px < 0 or py < 0: continue
            try:
                ts[py][px] = "rhs"
            except IndexError:
                pass

    which_touches = None
    flood = []
    for y in range(len(ts)):
        for x in range(len(ts[y])):
            if (x,y) not in visited and t is not None:
                flood.append((x,y))
            
    flooded = set()
    while flood:
        x,y = flood.pop()
        if (x,y) in flooded: continue
        else: flooded.add((x,y))

        if (x,y) in visited: continue
        if ts[y][x] is None: continue

        for dx,dy in [(0,-1),(0,1),(1,0),(-1,0)]:
            xp,yp = x+dx,y+dy

            if xp < 0 or xp >= len(ts[y]) or yp < 0 or yp >= len(ts):
                if which_touches is None:
                    which_touches = ts[y][x]
                continue

            if (xp,yp) not in visited:
                flood.append((xp,yp))
                ts[yp][xp] = ts[y][x]
        
    return sum(1 for y in range(len(ts)) for x in range(len(ts[y])) if (x,y) not in visited and ts[y][x] != which_touches)
