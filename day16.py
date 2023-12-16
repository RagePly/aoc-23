from collections import defaultdict
def part1(src):
    m = [[c for x,c in enumerate(l)] for y,l in enumerate(src.splitlines())]
    h,w = len(m), len(m[0])
    mirrors = {(x,y): c for y,l in enumerate(m) for x,c in enumerate(l) if c!='.'}
    beams = defaultdict(list) 

    UP,RIGHT,DOWN,LEFT = 0,1,2,3
    paths = [(0,0,RIGHT)]

    while paths:
        x,y,d = paths.pop()
        
        p = beams[x,y]
        if d in p:
            continue

        p.append(d)
        t = mirrors.get((x,y), '.')

        nd = []
        if t == '.':
            nd = [d]
        elif t == "|":
            if d == UP or d == DOWN:
                nd = [d]
            elif d == LEFT or d == RIGHT:
                nd = [UP,DOWN]
        elif t == "-":
            if d == UP or d == DOWN:
                nd = [LEFT,RIGHT]
            elif d == LEFT or d == RIGHT:
                nd = [d]
        elif t == "/":
            if d == UP:
                nd = [RIGHT]
            elif d == RIGHT:
                nd = [UP]
            elif d == DOWN:
                nd = [LEFT]
            elif d == LEFT:
                nd = [DOWN]
        elif t == "\\":
            if d == UP:
                nd = [LEFT]
            elif d == RIGHT:
                nd = [DOWN]
            elif d == DOWN:
                nd = [RIGHT]
            elif d == LEFT:
                nd = [UP]
        
        for dd in nd:
            if dd == UP:
                nx,ny = (x,y-1)
            elif dd == RIGHT:
                nx,ny = (x+1,y)
            elif dd == DOWN: 
                nx,ny = (x,y+1)
            elif dd == LEFT:
                nx,ny = (x-1,y)
            
            if not (nx < 0 or nx >= w or ny < 0 or ny >= h):
               paths.append((nx,ny,dd)) 
            
    return len(beams)
            

from itertools import repeat
def part2(src):
    m = [[c for x,c in enumerate(l)] for y,l in enumerate(src.splitlines())]
    h,w = len(m), len(m[0])
    mirrors = {(x,y): c for y,l in enumerate(m) for x,c in enumerate(l) if c!='.'}
    
    UP,RIGHT,DOWN,LEFT = 0,1,2,3
    mp = 0
    for sd in (UP,RIGHT,DOWN,LEFT):
        xs,ys = (range(w), repeat(h-1 if sd == UP else 0)) if sd in (UP,DOWN) else (repeat(w-1 if sd == LEFT else 0), range(w))
        for x,y in zip(xs,ys):
            beams = defaultdict(list) 
            paths = [(x,y,sd)]

            while paths:
                x,y,d = paths.pop()
                
                p = beams[x,y]
                if d in p:
                    continue

                p.append(d)
                t = mirrors.get((x,y), '.')

                nd = []
                if t == '.':
                    nd = [d]
                elif t == "|":
                    if d == UP or d == DOWN:
                        nd = [d]
                    elif d == LEFT or d == RIGHT:
                        nd = [UP,DOWN]
                elif t == "-":
                    if d == UP or d == DOWN:
                        nd = [LEFT,RIGHT]
                    elif d == LEFT or d == RIGHT:
                        nd = [d]
                elif t == "/":
                    if d == UP:
                        nd = [RIGHT]
                    elif d == RIGHT:
                        nd = [UP]
                    elif d == DOWN:
                        nd = [LEFT]
                    elif d == LEFT:
                        nd = [DOWN]
                elif t == "\\":
                    if d == UP:
                        nd = [LEFT]
                    elif d == RIGHT:
                        nd = [DOWN]
                    elif d == DOWN:
                        nd = [RIGHT]
                    elif d == LEFT:
                        nd = [UP]
                
                for dd in nd:
                    if dd == UP:
                        nx,ny = (x,y-1)
                    elif dd == RIGHT:
                        nx,ny = (x+1,y)
                    elif dd == DOWN: 
                        nx,ny = (x,y+1)
                    elif dd == LEFT:
                        nx,ny = (x-1,y)
                    
                    if not (nx < 0 or nx >= w or ny < 0 or ny >= h):
                       paths.append((nx,ny,dd)) 
                    
            mp = max(mp,len(beams))
    return mp

