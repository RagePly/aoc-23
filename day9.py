def nexth(history):
    for i in range(len(history) - 1):
        a,b = history[i:i+2]
        yield b-a

def evalhist(history):
    hh = [history]
    while not all(x == 0 for x in hh[-1]):
        hh.append(list(nexth(hh[-1])))
    hh[-1].append(0)

    for i in range(len(hh)-1):
        d = hh[-i-1][-1]
        hh[-i-2].append(hh[-i-2][-1] + d)
    return hh[0][-1]

def part1(src):
    s = 0
    for line in src.splitlines():
        history = map(int, line.split())
        s += evalhist(list(history))
    return s

def evalhistr(history):
    hh = [history]
    while not all(x == 0 for x in hh[-1]):
        hh.append(list(nexth(hh[-1])))
    for h in hh:
        h.reverse()
    hh[-1].append(0)

    for i in range(len(hh)-1):
        d = hh[-i-1][-1]
        hh[-i-2].append(hh[-i-2][-1] - d)
    return hh[0][-1]

def part2(src):
    s = 0
    for line in src.splitlines():
        history = map(int, line.split())
        s += evalhistr(list(history))
    return s

