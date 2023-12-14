# import matplotlib.pyplot as plt

def part1(src):
    balls = []
    pipes = set()
    stuck = set()

    m = list(map(list,src.splitlines()))
    for y,line in enumerate(m):
        for x,c in enumerate(line):
            if c == "O":
                balls.append((y,x))
            elif c == "#":
                pipes.add((y,x))
    balls.sort()
    
    while balls:
        new_balls = []
        for (y,x) in balls:
            if y == 0 or (y-1,x) in pipes or (y-1,x) in stuck:
                stuck.add((y,x))
            else:
                new_balls.append((y-1,x))
        new_balls.sort()
        balls = new_balls


    s = 0
    for (y,x) in stuck:
        s += len(m)-y
    return s


def part2(src):
    balls = []
    pipes = set()
    stuck = set()

    loads = []
    m = list(map(list,src.splitlines()))
    for y,line in enumerate(m):
        for x,c in enumerate(line):
            if c == "O":
                stuck.add((y,x))
            elif c == "#":
                pipes.add((y,x))
    for k in range(1000000000):
        for ty,tx in [(-1,0), (0,-1), (1,0), (0,1)]:
            key = lambda b: b[abs(tx)]
            rev = ty == 1 or tx == 1

            balls = list(sorted(stuck, key=key,reverse=rev))
            stuck = set()

            while balls:
                new_balls = []
                for (y,x) in balls:
                    dy,dx = y+ty,x+tx
                    if dy < 0 or dy>=len(m) or dx < 0 or dx >= len(m[0]) or (dy,dx) in pipes or (dy,dx) in stuck:
                        stuck.add((y,x))
                    else:
                        new_balls.append((dy,dx))
                new_balls.sort(key=key, reverse=rev)
                balls = new_balls
              
        s = 0
        for (y,x) in stuck:
            s += len(m)-y
        loads.append(s)

        for n in range(5,10):
            if loads[-n:] == loads[-n*2:-n]:
                rcycles = 1000000000 - k - 2
                return loads[-n:][rcycles%n]
