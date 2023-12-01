def part1(src):
    s = 0
    for line in src.splitlines():
        digits = list(filter(str.isdigit, line))
        s += int(digits[0] + digits[-1])
    return s

def findallof(s, ss):
    matches = []
    j = 0
    while True:
        j = s.find(ss, j)
        if j == -1: break

        matches.append(j)
        j += 1
    return matches

def part2(src):
    s = 0
    names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in src.splitlines():
        digits = [(i, n) for i, n in enumerate(line) if n.isdigit()]

        for nv, n in enumerate(names):
            for i in findallof(line, n):
                digits.append((i, str(nv+1)))
        
        digits.sort()
        s += int(digits[0][1] + digits[-1][1])
    return s
