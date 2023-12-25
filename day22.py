from collections import namedtuple, defaultdict, deque

def part1(src):
    pos = namedtuple("pos", "x, y, z")
    bricks = []
    xmax,xmin,ymax,ymin,zmax,zmin = [0,100000]*3
    for nr, line in enumerate(src.splitlines()):
        name = line # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[nr]
        (x,y,z), (i,j,k) = map(lambda s: map(int, s.split(",")), line.split("~"))
        dx = 0 if i-x == 0 else (i-x)//abs(i-x)
        dy = 0 if j-y == 0 else (j-y)//abs(j-y)
        dz = 0 if k-z == 0 else (k-z)//abs(k-z)

        xmax, xmin = max(x,i,xmax), min(x,i,xmin)
        ymax, ymin = max(y,j,ymax), min(y,j,ymin)
        zmax, zmin = max(z,k,zmax), min(z,k,zmin)

        d = pos(dx,dy,dz)
        p = pos(x,y,z)
        e = pos(i,j,k)

        brick = [p]
        while p != e:
            p = pos(p.x + d.x, p.y + d.y, p.z + d.z)
            brick.append(p)
        brick.sort(key=lambda p: p.z)
        bricks.append((brick, name))

    bricks.sort(key=lambda b: b[0][0].z)
    floor = [[(0, None) for _ in range(xmin,xmax+1)] for _ in range(ymin, ymax+1)]
    supports = set()

    for brick,name in bricks:
        dz = None 
        for p in brick:
            d = p.z - floor[p.y][p.x][0] - 1
            assert d >= 0
            if dz is None or d < dz:
                dz = d if dz is None else min(d, dz)
        rested_on = set()
        for p in brick:
            nz = p.z - dz
            if (below := floor[p.y][p.x][1]) and below != name and floor[p.y][p.x][0] == nz - 1:
                rested_on.add(below)
            floor[p.y][p.x] = nz, name
        if len(rested_on) == 1:
            supports.add(rested_on.pop())

    return len(bricks) - len(supports)

def part2(src):
    pos = namedtuple("pos", "x, y, z")
    bricks = []
    xmax,xmin,ymax,ymin,zmax,zmin = [0,100000]*3
    for nr, line in enumerate(src.splitlines()):
        name = line # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[nr]
        (x,y,z), (i,j,k) = map(lambda s: map(int, s.split(",")), line.split("~"))
        dx = 0 if i-x == 0 else (i-x)//abs(i-x)
        dy = 0 if j-y == 0 else (j-y)//abs(j-y)
        dz = 0 if k-z == 0 else (k-z)//abs(k-z)

        xmax, xmin = max(x,i,xmax), min(x,i,xmin)
        ymax, ymin = max(y,j,ymax), min(y,j,ymin)
        zmax, zmin = max(z,k,zmax), min(z,k,zmin)

        d = pos(dx,dy,dz)
        p = pos(x,y,z)
        e = pos(i,j,k)

        brick = [p]
        while p != e:
            p = pos(p.x + d.x, p.y + d.y, p.z + d.z)
            brick.append(p)
        brick.sort(key=lambda p: p.z)
        bricks.append((brick, name))

    bricks.sort(key=lambda b: b[0][0].z)
    floor = [[(0, None) for _ in range(xmin,xmax+1)] for _ in range(ymin, ymax+1)]
    above = defaultdict(set)
    under = defaultdict(set)
    supports = set()

    for brick,name in bricks:
        dz = None 
        for p in brick:
            d = p.z - floor[p.y][p.x][0] - 1
            assert d >= 0
            if dz is None or d < dz:
                dz = d if dz is None else min(d, dz)
        for p in brick:
            nz = p.z - dz
            if (below := floor[p.y][p.x][1]) and below != name and floor[p.y][p.x][0] == nz - 1:
                above[below].add(name)
                under[name].add(below)
            floor[p.y][p.x] = nz, name
        if len(under[name]) == 1:
            supports.add(next(iter(under[name])))

    s = 0
    for brick in supports:
        desintegrated = set([brick])
        queue = deque()
        for b in above[brick]:
            queue.append(b)

        while queue:
            b = queue.popleft()
            if under[b] <= desintegrated:
                desintegrated.add(b)
                for bc in above[b]:
                    queue.append(bc)
        s += len(desintegrated) - 1
    return s
