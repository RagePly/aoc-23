from collections import deque, defaultdict
from math import lcm

def part1(src):
    graph = {}
    for line in src.splitlines():
        source, dests = line.split(" -> ")
        dests = dests.split(", ")

        if source.startswith("%"):
            graph[source[1:]] = ["%", False, dests]
        elif source.startswith("&"):
            graph[source[1:]] = ["&", {}, dests]
        else:
            graph[source] = ["~", None, dests]

    graph["button"] = ("~", None, ["broadcaster"])
    
    for n, [_, _, dests] in graph.items():
        for dest in dests:
            if dest in graph:
                [v, state, _] = graph[dest]
                if v == "&": state[n] = False

    hpulse = 0
    lpulse = 0
    for _ in range(1000):
        queue = deque()
        queue.append(("button", False, ""))
        while queue:
            n, signal, prevn = queue.popleft()
            if n not in graph: continue
            t, state, children = graph[n]

            if t == "~":
                new_signal = signal
            elif t == "%" and not signal:
                graph[n][1] = not state
                new_signal = not state
            elif t == "&":
                state[prevn] = signal
                new_signal = not all(state.values())
            else:
                continue

            if new_signal:
                hpulse += len(children)
            else:
                lpulse += len(children)

            for child in children:
                # print(f"{t}{n} -{new_signal}-> {child}")
                queue.append((child, new_signal, n))
        # print(hpulse,lpulse)
    return hpulse*lpulse

def part2(src):
    graph = defaultdict(list)
    igraph = defaultdict(list)
    for line in src.splitlines():
        source, dests = line.split(" -> ")
        dests = dests.split(", ")
        n = source[1:] if "%" in source or "&" in source else source
        for d in dests:
            graph[n].append(d)
            igraph[d].append(n)
    gates = [igraph[n][0] for n in igraph[igraph["rx"][0]]]
    
    numbers = []
    for lsf in graph["broadcaster"]:
        queue = deque()
        queue.append(lsf)
        number = 0
        mask = 1
        while queue:
            n = queue.popleft() 
            for d in graph[n]:
                if d in gates:
                    number |= mask
                else:
                    queue.append(d)
            mask <<= 1
        numbers.append(number)
    return lcm(*numbers)
