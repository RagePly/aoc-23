from collections import Counter, defaultdict
from functools import cmp_to_key
def part1(src):
    order = list(reversed(('A','K','Q','J','T','9','8','7','6','5','4','3','2')))
    s = 0
    hands = []
    for line in src.splitlines():
        hand, bid = line.strip().split()
        bid = int(bid)
        c = Counter(hand)
        cc = defaultdict(list)
        for v, i in c.items():
            cc[i].append(v)
        hands.append((cc, hand, bid))
    
    def go(c):
        nonlocal order
        return order.index(c)

    def byorder(o1,o2):
        for c1,c2 in zip(map(go, o1), map(go, o2)):
            if c1 > c2:
                return True
            elif c1 < c2:
                return False
        assert False
            
    def oh(h1, h2):
        c1, o1, _ = h1
        c2, o2, _ = h2

        if 5 in c1 or 5 in c2:
            if 5 in c1 and 5 in c2:
                return byorder(o1,o2)
            elif 5 in c1:
                return True
            return False
        elif 4 in c1 or 4 in c2:
            if 4 in c1 and 4 in c2:
                return byorder(o1,o2)
            elif 4 in c1:
                return True
            return False
        elif (3 in c1 and 2 in c1) or (3 in c2 and 2 in c2):
            if (3 in c1 and 2 in c1) and (3 in c2 and 2 in c2):
                return byorder(o1,o2)
            elif 3 in c1 and 2 in c1:
                return True
            return False
        elif 3 in c1 or 3 in c2:
            if 3 in c1 and 3 in c2:
                return byorder(o1,o2)
            elif 3 in c1:
                return True
            return False
        elif (2 in c1 and len(c1[2]) == 2) or (2 in c2 and len(c2[2]) == 2):
            if (2 in c1 and len(c1[2]) == 2) and (2 in c2 and len(c2[2]) == 2):
                return byorder(o1,o2)
            elif (2 in c1 and len(c1[2]) == 2):
                return True
            return False
        elif 2 in c1 or 2 in c2:
            if 2 in c1 and 2 in c2:
                return byorder(o1,o2)
            elif 2 in c1:
                return True
            return False
        return byorder(o1,o2)

    def sf(h1,h2):
        if oh(h1,h2):
            return 1
        return -1
    
    hands.sort(key=cmp_to_key(sf))
    return sum((i+1)*b for i, (_, _, b) in enumerate(hands))

def part2(src):
    order = list(reversed(('A','K','Q','T','9','8','7','6','5','4','3','2','J')))
    s = 0
    hands = []
    for line in src.splitlines():
        hand, bid = line.strip().split()
        bid = int(bid)
        c = Counter(hand)
        cc = defaultdict(list)
        jokers = []
        for v, i in c.items():
            if v == 'J':
                jokers.append((v,i))
            else:
                cc[i].append(v)
        for v, i in jokers:
            if not cc:
                cc[i] = [v]
            else:
                n = max(cc.keys())
                if len(cc[n]) > 1:
                    c = cc[n].pop()
                    cc[n+i] = [c]
                else:
                    cc[n+i] = cc[n]
                    del cc[n]

        hands.append((cc, hand, bid))
    
    def go(c):
        nonlocal order
        return order.index(c)

    def byorder(o1,o2):
        for c1,c2 in zip(map(go, o1), map(go, o2)):
            if c1 > c2:
                return True
            elif c1 < c2:
                return False
        assert False
            
    def oh(h1, h2):
        c1, o1, _ = h1
        c2, o2, _ = h2

        if 5 in c1 or 5 in c2:
            if 5 in c1 and 5 in c2:
                return byorder(o1,o2)
            elif 5 in c1:
                return True
            return False
        elif 4 in c1 or 4 in c2:
            if 4 in c1 and 4 in c2:
                return byorder(o1,o2)
            elif 4 in c1:
                return True
            return False
        elif (3 in c1 and 2 in c1) or (3 in c2 and 2 in c2):
            if (3 in c1 and 2 in c1) and (3 in c2 and 2 in c2):
                return byorder(o1,o2)
            elif 3 in c1 and 2 in c1:
                return True
            return False
        elif 3 in c1 or 3 in c2:
            if 3 in c1 and 3 in c2:
                return byorder(o1,o2)
            elif 3 in c1:
                return True
            return False
        elif (2 in c1 and len(c1[2]) == 2) or (2 in c2 and len(c2[2]) == 2):
            if (2 in c1 and len(c1[2]) == 2) and (2 in c2 and len(c2[2]) == 2):
                return byorder(o1,o2)
            elif (2 in c1 and len(c1[2]) == 2):
                return True
            return False
        elif 2 in c1 or 2 in c2:
            if 2 in c1 and 2 in c2:
                return byorder(o1,o2)
            elif 2 in c1:
                return True
            return False
        return byorder(o1,o2)

    def sf(h1,h2):
        if oh(h1,h2):
            return 1
        return -1
    
    hands.sort(key=cmp_to_key(sf))
    return sum((i+1)*b for i, (_, _, b) in enumerate(hands))
