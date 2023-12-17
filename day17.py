from heapq import heappush, heappop
from collections import defaultdict
def mh(x,y,nx,ny):
    return abs(x-nx) + abs(y-ny)

def part1(src):
    grid = [[int(c) for c in line] for line in src.splitlines()]
    
    UP,RIGHT,DOWN,LEFT = 0,1,2,3
    camefrom = {}
    scores = defaultdict(lambda: [100000000000000000000000000 for _ in range(4 * 4)])
    queue = [(mh(0,0,len(grid[0]),len(grid)), 0, 0, 0, DOWN, 0, 0)]
    i = 1

    while queue:
        thl, hl, pi, c, d, x, y = heappop(queue)

        if y == len(grid) - 1 and x == len(grid) - 1:
            return hl
        
        if scores[x,y][c * 4 + d] <= hl:
            continue
        scores[x,y][c * 4 + d] = hl

        for nd,(dx,dy) in enumerate([(0,-1),(1,0),(0,1),(-1,0)]):
            nx,ny = x+dx,y+dy
            if (d-nd) % 4 == 2: continue # backwards
            elif nd == d and c == 3: continue 
            elif nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid): continue
            
            nc = c+1 if nd == d else 1
            nhl = hl + grid[ny][nx]
            nthl = nhl + mh(nx,ny,len(grid[0]),len(grid))
            heappush(queue,(nthl, nhl, i, nc, nd, nx, ny))
            i += 1

def part2(src):
    grid = [[int(c) for c in line] for line in src.splitlines()]
    
    UP,RIGHT,DOWN,LEFT = 0,1,2,3
    camefrom = {}
    scores = [[[100000000000000000000000000 for _ in range(11 * 4)] for _ in line] for line in grid]
    queue = [(mh(0,0,len(grid[0]),len(grid)), 0, 0, 0, DOWN, 0, 0)]
    i = 1

    while queue:
        thl, hl, pi, c, d, x, y = heappop(queue)

        if y == len(grid) - 1 and x == len(grid) - 1:
            return hl
        
        if scores[y][x][c * 4 + d] <= hl:
            continue
        scores[y][x][c * 4 + d] = hl

        for nd,(dx,dy) in enumerate([(0,-1),(1,0),(0,1),(-1,0)]):
            nx,ny = x+dx,y+dy
            if (d-nd) % 4 == 2: continue # backwards
            elif nd == d and c == 10: continue 
            elif nd != d and c > 0 and c < 4: continue
            elif nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid): continue
            
            nc = c+1 if nd == d else 1
            nhl = hl + grid[ny][nx]
            nthl = nhl + mh(nx,ny,len(grid[0]),len(grid))
            heappush(queue,(nthl, nhl, i, nc, nd, nx, ny))
            i += 1

