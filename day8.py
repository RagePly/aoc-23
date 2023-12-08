def part1(src):
    nodes = {}
    rules, g = src.split("\n\n")
    for line in g.splitlines():
        n, p = line.split(" = ")
        nl, nr = p[1:-1].split(", ")
        nodes[n] = (nl,nr)

    i = 0
    n = "AAA"
    while True:
        r = rules[i%len(rules)]
        i+=1

        if r == "L":
            n = nodes[n][0]
        else:
            n = nodes[n][1]

        if n == "ZZZ":
            break
    return i

def find_cycle(start, graph, rules):
    i = 0
    n = start
    at_z = None
    while at_z is None:
        r = rules[i%len(rules)]
        if r == "L":
            n = graph[n][0]
        else:
            n = graph[n][1]

        i+=1
        if n.endswith("Z"):
            at_z = i
    return at_z
        
import math
def part2(src):
    nodes = {}
    rules, g = src.split("\n\n")
    for line in g.splitlines():
        n, p = line.split(" = ")
        nl, nr = p[1:-1].split(", ")
        nodes[n] = (nl,nr)
    
    na = [n for n in nodes.keys() if n.endswith("A")]
    
    return math.lcm(*(find_cycle(n, nodes, rules) for n in na))

