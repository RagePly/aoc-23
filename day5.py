from collections import defaultdict
def part1(src):
    seeds, *ratios = src.split("\n\n")
    _, *seeds = seeds.split()
    
    maps = dict()
    for ratio in ratios:
        mapping, *rs = ratio.splitlines()
        s, _, d, *_ = mapping.split()[0].split("-")
        maps[s] = (d, [tuple(map(int, r.split())) for r in rs])

    m = None
    for s in map(int, seeds):
        c = "seed"
        while c != "location":
            nc, rs = maps[c]
            for dr, sr, l in rs:
                if sr <= s and s < sr + l:
                    s += (dr - sr)
                    break
            c = nc
        m = s if m is None else min(s, m)

    return m

from heapq import heappop, heappush
def part2(src):
    seeds, *ratios = src.split("\n\n")
    _, *seeds = seeds.split()
    seeds = [(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1) for i in range(0, len(seeds), 2)]
    
    maps = dict()
    for ratio in ratios:
        mapping, *rs = ratio.splitlines()
        s, _, d, *_ = mapping.split()[0].split("-")
        maps[s] = (d, [tuple(map(int, r.split())) for r in rs])
    
    traversal = ['seed']
    while traversal[-1] != 'location':
        traversal.append(maps[traversal[-1]][0])
    order = {l: i for i,l in enumerate(traversal)}

    queue = []
    for a, b in seeds:
        heappush(queue, (order['seed'], a, b, 'seed'))
    visited = set()
    
    while queue:
        hp = heappop(queue)
        if hp in visited: continue
        else: visited.add(hp)

        o, a, b, c = hp
        if b < a: continue

        if c == "location":
            return a
                
        nc,rs = maps[c]
        no = order[nc]
        f = True
        for dp, sp, lp in rs:
            ap, bp = sp, sp+lp-1
            d = dp - sp 
            if b < ap or bp < a:
                continue
            elif ap <= a and b <= bp:
                heappush(queue, (no, a+d, b+d, nc))
            elif a <= ap and bp <= b:
                heappush(queue, (o, a, ap-1, c))
                heappush(queue, (o, bp+1, b, c))
                heappush(queue, (no, ap+d, bp+d, nc))
            elif a <= ap:
                heappush(queue, (o, a, ap-1, c))
                heappush(queue, (no, ap+d, b+d, nc))
            else:
                heappush(queue, (o, bp+1, b, c))
                heappush(queue, (no, a+d, bp+1+d, nc))
            f = False
        if f:
            heappush(queue, (no, a, b, nc))
    return None
