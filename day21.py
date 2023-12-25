def part1(src):
    m = list(map(list, src.splitlines()))
    s = next((x,y) for y,l in enumerate(m) for x,s in enumerate(l) if s == "S")
    h,w = len(m), len(m[0])
    
    steps = set([s]) 

    for _ in range(64):
        new_steps = set()
        for x,y in steps:
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if nx >= 0 and nx < w and ny >= 0 and ny < h and m[ny][nx] != "#":
                    new_steps.add((nx,ny))
        steps = new_steps
    
    return len(steps)
def printmap(m,active,xo,yo, xstart, xend, ystart, yend):
    print("\x1b[2J\x1b[H",end="")
    for y in range(ystart, yend+1):
        for x in range(xstart, xend+1):
            if (x,y) in active:
                print("O", end="")
            else:
                print(m[(y+yo)%len(m)][(x+xo)%len(m[0])],end="")
        print()

from collections import defaultdict
from time import sleep

def part2(src):
    m = list(map(list, src.splitlines()))
    s = next((x,y) for y,l in enumerate(m) for x,s in enumerate(l) if s == "S")
    h,w = len(m), len(m[0])

    def runsteps(n,steps):
        for _ in range(n): # (w-1)//2 + w):
            new_steps = set()
            for x,y in steps:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = x+dx,y+dy
                    if m[ny%h][nx%w] != "#":
                        new_steps.add((nx,ny))
            steps = new_steps
        return steps

    steps = set([s]) 
    n = 65
    X = w
    steps = runsteps(65, steps)
    fn0x = len(steps)
    steps =  runsteps(X, steps)
    fn1x = len(steps)
    steps = runsteps(X, steps)
    fn2x = len(steps)
    
    """
        f(x) = a x² + b x + c

        f(n) = a n² + b n + c
        c = f(n) - a n² - b n

        f(n+X) = a (n+X)² + b (n+X) + c 
               = a n² + 2 a X n + a X² + b n + b X + c
               = a n² + 2 a X n + a X² + b n + b X + f(n) - a n² - b n
               = 2 a X n + a X² + b X + f(n)
           b X = f(n+X) - f(n) - 2 a X n - a X²

        f(n+2X) = a (n+2X)² + b (n+2X) + c 
                = a n² + 4 a X n + 4 a X² + b n + 2 b X + c
                = a n² + 4 a X n + 4 a X² + b n + 2 b X + f(n) - a n² - b n
                = 4 a X n + 4 a X² + 2 b X + f(n)
                = 4 a X n + 4 a X² + 2 (f(n+X) - f(n) - 2 a X n - a X²) + f(n)
                = 4 a X n + 4 a X² + 2 f(n+X) - 2 f(n) - 4 a X n - 2 a X² + f(n)
                = 2 a X² + 2 f(n+X) - f(n)
            a X = (f(n+2X) - 2 (fn+X) + f(n)) / 2X

    """

    a = (fn2x - 2 * fn1x + fn0x) / (2 * X**2)
    b = (fn1x - fn0x - 2 * a * X * n - a * X**2) / X
    c = fn0x - a * n**2 - b * n

    x = 26501365
    return a*x**2 + b*x + c
