def part1(src):
    s = 0 
    for line in src.splitlines():
        _, cards = line.split(": ")
        card, my = map(lambda p: set(map(int, p.split())), cards.split(" | "))
        common = card & my
        if common:
            s += 2 ** (len(common) - 1)
    return s

from collections import defaultdict 
def part2(src):
    s = 0 
    copies = defaultdict(int)
    for i, line in enumerate(src.splitlines()):
        _, cards = line.split(": ")
        card, my = map(lambda p: set(map(int, p.split())), cards.split(" | "))
        common = len(card & my)

        copies[i] += 1
        for j in range(i + 1, i + common + 1):
            copies[j] += copies[i]
            
    return sum(copies.values())

