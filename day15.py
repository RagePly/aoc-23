def he(s):
    h = 0
    for c in s:
        h+=ord(c)
        h*=17
        h%=256
    return h

def part1(src):
    s = 0
    for line in src.strip().split(","):
        s += he(line)
    return s

from collections import defaultdict
def part2(src):
    boxes = defaultdict(dict)
    for i,line in enumerate(src.strip().split(",")):
        if line.endswith("-"):
            l = line[:-1]
            h = he(l)
            if l in boxes[h]:
                del boxes[h][l]
        else:
            l,n = line.split("=")
            h = he(l)
            boxes[h][l] = (boxes[h].get(l, (i, None))[0], int(n))
    s = 0
    for b,ls in boxes.items():
        slots = sorted(ls.values())
        for i,(_, n) in enumerate(slots):
            s += (b+1) * (i+1) * n
    return s
