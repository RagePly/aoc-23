
def part1(src):
    s = 0
    for line in src.splitlines():
        game, drafts = line.split(': ')
        _, gid = game.split()
        for subset in drafts.split("; "):
            for cubes in subset.split(", "):
                n, col = cubes.split(); n = int(n)
                if col == "red" and n > 12: break
                elif col == "green" and n > 13: break
                elif col == "blue" and n > 14: break
            else: continue
            break
        else: s += int(gid)
    return s

def part2(src):
    s = 0
    for line in src.splitlines():
        _, drafts = line.split(': ')
        red, green, blue = 0, 0, 0
        for subset in drafts.split("; "):
            for cubes in subset.split(", "):
                n, col = cubes.split(); n = int(n)
                if col == "red":
                    red = max(n, red)
                elif col == "green":
                    green = max(n, green)
                elif col == "blue":
                    blue = max(n, blue)
        s += red * green * blue
    return s
