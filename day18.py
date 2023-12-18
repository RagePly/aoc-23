from itertools import chain
def part1(src):
    holes = {(0,0)}

    xmax,ymax = 0,0
    xmin,ymin = 0,0
    x,y = 0,0
    for line in src.splitlines():
        d, n, _ = line.split()
        for _ in range(int(n)):
            if d == "U":
                x,y = x,y-1
            elif d == "D":
                x,y = x,y+1
            elif d == "R":
                x,y = x+1,y
            else:
                x,y = x-1,y

            xmax,ymax = max(xmax,x),max(ymax,y)
            xmin,ymin = min(xmin,x),min(ymin,y)
            holes.add((x,y))
    
    points = filter(
            lambda p: p not in holes,
            chain(
                ((x,y) for y in range(ymin,ymax+1) for x in [xmin,xmax]),
                ((x,y) for y in [ymin,ymax] for x in range(xmin,xmax+1)))
            )
        
    queue = list(points)
    outside = set()
    while queue:
        x,y = queue.pop()
        if x < xmin or x > xmax or y < ymin or y > ymax:
            continue
        elif (x,y) in outside:
            continue
        outside.add((x,y))  
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if (nx,ny) in holes: continue
            queue.append((nx,ny))

    s = 0
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            if (x,y) not in outside:
                s += 1
    return s

    
from aoctools.datastruct.shapes import box
def part2(src):
    block = 0
    cuts = []
    xmax,ymax = 0,0
    xmin,ymin = 0,0
    x,y = 0,0
    for line in src.splitlines():
        h = line.split()[-1][2:-1]
        l = int(h[:5],base=16)
        d = "RDLU"[int(h[-1], base=16)]
        
        nx,ny = x,y
        match d:
            case "R":
                nx = x+l
                cuts.append(box(x,nx,y,y))
            case "L":
                nx = x-l
                cuts.append(box(nx,x,y,y))
            case "D":
                ny = y+l
                cuts.append(box(x,x,y,ny))
            case "U":
                ny = y-l
                cuts.append(box(x,x,ny,y))
        x = nx
        y = ny
        xmax,ymax = max(xmax,x),max(ymax,y)
        xmin,ymin = min(xmin,x),min(ymin,y)
    
    boxes = [box(xmin,xmax,ymin,ymax)]

    for cut in cuts:
        newboxes = []
        for b in boxes:
            for nb in cut.cut(b):
                newboxes.append(nb)
        boxes = newboxes

    eliminate = []
    new_boxes = []
    for i,b in enumerate(boxes):
        if b.h.a == xmin or b.h.b == xmax or b.v.a == ymin or b.v.b == ymax:
            eliminate.append(b)
            continue
        else:
            new_boxes.append(b)

    boxes = new_boxes
    eliminated = []
    while eliminate:
        b = eliminate.pop()
        eliminated.append(b) 

        new_boxes = []
        for ob in boxes:
            if ((b.h.a - 1 == ob.h.b and b.v.intersection(ob.v) is not None) or
                (b.h.b + 1 == ob.h.a and b.v.intersection(ob.v) is not None) or
                (b.v.a - 1 == ob.v.b and b.h.intersection(ob.h) is not None) or
                (b.v.b + 1 == ob.v.a and b.h.intersection(ob.h) is not None)):
                eliminate.append(ob)
            else: new_boxes.append(ob)
        boxes = new_boxes

    s = (xmax-xmin+1)*(ymax-ymin+1)
    for b in eliminated:
        s -= (b.h.b-b.h.a+1) * (b.v.b-b.v.a+1)

    return s
    
