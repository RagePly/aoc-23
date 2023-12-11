def part1(src):
    m = [((x,y), c) for y, line in enumerate(src.splitlines()) for x,c in enumerate(line) ]
    empty = [p for p,v in m if v == "."]
    full = [p for p,v in m if v == "#"]

    full_x = set(p[0] for p in full)
    full_y = set(p[1] for p in full)

    empty_x = set(p[0] for p in empty)
    empty_y = set(p[1] for p in empty)

    expanded_rows = list(sorted(empty_y - full_y))
    expanded_col = list(sorted(empty_x - full_x))

    new_pos = []
    for (x,y) in full:
        new_x = x
        for xp in expanded_col:
            if x < xp:
                break
            new_x+=1
        new_y = y
        for yp in expanded_rows:
            if y < yp:
                break
            new_y+=1
        new_pos.append((new_x,new_y))

    dist = 0
    for i in range(len(new_pos)-1):
        a = new_pos[i]
        for j in range(i+1, len(new_pos)):
            b = new_pos[j]
            dist += abs(a[0] - b[0])
            dist += abs(a[1] - b[1])
    return dist
    
def part2(src):
    m = [((x,y), c) for y, line in enumerate(src.splitlines()) for x,c in enumerate(line) ]
    empty = [p for p,v in m if v == "."]
    full = [p for p,v in m if v == "#"]

    full_x = set(p[0] for p in full)
    full_y = set(p[1] for p in full)

    empty_x = set(p[0] for p in empty)
    empty_y = set(p[1] for p in empty)

    expanded_rows = list(sorted(empty_y - full_y))
    expanded_col = list(sorted(empty_x - full_x))

    new_pos = []
    for (x,y) in full:
        new_x = x
        for xp in expanded_col:
            if x < xp:
                break
            new_x+=1000000-1
        new_y = y
        for yp in expanded_rows:
            if y < yp:
                break
            new_y+=1000000-1
        new_pos.append((new_x,new_y))

    dist = 0
    for i in range(len(new_pos)-1):
        a = new_pos[i]
        for j in range(i+1, len(new_pos)):
            b = new_pos[j]
            dist += abs(a[0] - b[0])
            dist += abs(a[1] - b[1])
    return dist

