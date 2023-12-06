from math import sqrt
def part1(src):
    ts, ds = (list(map(int, l.split()[1:])) for l in src.splitlines())
    s = 1
    for t, d in zip(ts, ds):
        wins = 0
        for hold in range(t):
            r = t - hold
            dist = r * hold 
            if dist > d:
                wins += 1
        s *= wins
    return s


def part2(src):
    t, d = (int("".join(l.split()[1:])) for l in src.splitlines())
    wins = 0
    
    # WARNING: taboo floating-point math below...
    h1 = sqrt(t*t/4 - d) + t/2
    h2 = -sqrt(t*t/4 - d) + t/2 + 1

    if int(h1) == h1:
        return int(h1) - int(h2)
    return int(h1+1) - int(h2)
