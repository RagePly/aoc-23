from collections import defaultdict

def part1(src):
    arrangements = defaultdict(list)
    handle = []
    for i, line in enumerate(src.splitlines()):
        m,conf = line.split()
        conf = list(map(int, reversed(conf.split(","))))
        m = list(reversed(m))
        handle.append((i,m,0,False,conf,[]))

    while handle:
        i,m,active,n,conf,build = handle.pop()
        for _ in range(len(m)):
            c = m.pop()
            if c == ".":
                n = False
                if active > 0: break
                build.append(c)
            elif c == "#":
                if n: break

                if active == 0:
                    if not conf: break
                    active = conf.pop()
                active -= 1
                if active == 0:
                    n = True
                build.append('#')
            else:
                if active > 0: 
                    active -= 1
                    if active == 0:
                        n = True
                    build.append('#')
                elif n:
                    n = False
                    build.append('.')
                else:
                    handle.append((i, list(m), 0, n, list(conf),list(build + ['.'])))

                    if not conf: break

                    active = conf.pop() - 1

                    if active == 0: n = True
                    build.append('#')

        else:
            if active == 0 and not conf:
                arrangements[i].append(build)
            continue

    return sum(map(len, arrangements.values()))

import functools
def index(l,i,/,start=None,end=None,neg=False,default=None):
    start = 0 if start is None else start
    end = len(l) if end is None else end
    l = l[start:end]

    try:
        if neg:
            return start + next(filter(lambda x: x[1]!=i, enumerate(l)))[0]
        return start + l.index(i)
    except:
        return default

@functools.cache
def f(gs,m):
    if not m:
        if not gs:
            return 1
        return 0
    if not gs:
        if "#" in m:
            return 0
        return 1

    g,*gsr = gs
    if g > len(m):
        return 0

    s = 0
    fl = False
    if m[0] == "?":
        i = index(m,'.',start=1,neg=True,default=1) 
        fl = True
        s += f(gs,m[i:])

    if g < len(m) and m[g] == '#':
        return s

    d = len(m)+1 if (d:=index(m,'.')) is None else d
    if d < g:
        return s

    i = index(m,'.',start=g+1,neg=True,default=g+1) 
    return s + f(tuple(gsr),m[i:])


def part2(src):
    f.cache_clear() # for benchmark fairness
    arrangements = 0
    for i, line in enumerate(src.splitlines()):
        m,conf = line.split()
        gsold = tuple(map(int, conf.split(",")))
        gs = gsold*5
        mold = m
        m = ((m+'?')*5)[:-1]

        i = index(m,'.',neg=True,default=0) 
        t = f(gs,m[i:]) 

        arrangements += t
    return arrangements

