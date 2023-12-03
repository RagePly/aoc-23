from itertools import product
def part1(src):
    grid = list(map(list, src.splitlines()))
    h, w = len(grid), len(grid[0])
    s = 0

    visited = set()
    for x, y in product(range(w), range(h)):
        c = grid[y][x]
        if c == '.' or c.isdigit(): continue
        
        for dx,dy in product([-1,0,1], repeat=2):
            if dx == 0 and dy == 0: continue
            xp = x + dx
            yp = y + dy

            if 0 > xp or w <= xp: continue 
            if 0 > yp or h <= yp: continue 

            cp = grid[yp][xp]
            if not cp.isdigit(): continue
            start = xp 
            while start >= 0 and grid[yp][start].isdigit():
                start -= 1
            start += 1

            if (yp, start) in visited: continue
            visited.add((yp, start))

            end = xp 
            while end < w and grid[yp][end].isdigit():
                end += 1

            s += int("".join(grid[yp][start:end]))
    return s

def part2(src):
    grid = list(map(list, src.splitlines()))
    h, w = len(grid), len(grid[0])
    gears = {}

    for x, y in product(range(w), range(h)):
        c = grid[y][x]
        if c != '*': continue
        
        for dx,dy in product([-1,0,1], repeat=2):
            if dx == 0 and dy == 0: continue
            xp = x + dx
            yp = y + dy

            if 0 > xp or w <= xp: continue 
            if 0 > yp or h <= yp: continue 

            cp = grid[yp][xp]
            if not cp.isdigit(): continue

            start = xp 
            while start >= 0 and grid[yp][start].isdigit():
                start -= 1
            start += 1

            end = xp 
            while end < w and grid[yp][end].isdigit():
                end += 1

            gears[(x,y)] = gears.get((x, y), set()) | {(start, yp, int("".join(grid[yp][start:end])))}
    s = 0
    for g in gears.values():
        match list(g):
            case [(_, _, g1), (_, _, g2)]:
                s += g1*g2

    return s
