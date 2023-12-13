def part1(src):
    mirrors = src.split("\n\n")
    s = 0
    for mirror in mirrors:
        mirrormap_h = [list(c) for c in mirror.splitlines()]
        mirrormap_v = [list(reversed([mirrormap_h[y][x] for y in range(len(mirrormap_h))])) for x in range(len(mirrormap_h[0]))]
        for y in range(1,len(mirrormap_h)):
            h = min(y, len(mirrormap_h) - y)
            above,below = mirrormap_h[max(0, y-h):y], mirrormap_h[y:y+h]
            if not above: break

            if above == list(reversed(below)):
                s += 100 * y
                break

        for x in range(1,len(mirrormap_v)):
            w = min(x, len(mirrormap_v) - x)
            left,right = mirrormap_v[max(0, x-w):x], mirrormap_v[x:x+w]
            if not left: break
            if left == list(reversed(right)):
                s += x
                break
    return s

        
def part2(src):
    mirrors = src.split("\n\n")
    s = 0
    for mirror in mirrors:
        mirrormap_h = [list(c) for c in mirror.splitlines()]
        mirrormap_v = [list(reversed([mirrormap_h[y][x] for y in range(len(mirrormap_h))])) for x in range(len(mirrormap_h[0]))]

        def findmatch(m):
            for y in range(1,len(m)):
                h = min(y, len(m) - y)
                above,below = m[max(0, y-h):y], m[y:y+h]
                if not above: break

                missmatch = 0
                for a,b in zip(above, list(reversed(below))):
                    if missmatch > 1: break
                    for c1,c2 in zip(a,b):
                        if missmatch > 1: break
                        if c1 != c2:
                            missmatch += 1
                if missmatch == 1:
                    return y

        y = findmatch(mirrormap_h)
        x = findmatch(mirrormap_v)

        if x is not None:
            s += x
        if y is not None:
            s += y * 100
    return s

