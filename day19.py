def part1(src):
    instr, values = src.split("\n\n")

    vals = []

    instructions = {}
    for inst in instr.splitlines():
        name, comp = inst[:-1].split("{")
        comps = []
        for c in comp.split(","):
            if ":" not in c:
                comps.append((None, None, None, c))
                continue
            cond,ne = c.split(":")
            var = cond[0]
            op = cond[1]
            v = int(cond[2:])
            comps.append((var,op,v,ne))
        instructions[name] = comps

    s = 0
    for v in values.splitlines():
        val = {}
        for c in v[1:-1].split(","):
            k,i = c.split("=")
            val[k] = int(i)
        
        instr = "in"
        while instr not in ("R", "A"):
            for var,op,v,ne in instructions[instr]:
                if var is None:
                    instr = ne
                elif op == "<":
                    if val[var] < v:
                        instr = ne
                        break
                elif val[var] > v:
                    instr = ne
                    break
        if instr == "A":
            s += sum(val.values())
    return s 

from functools import reduce
def part2(src):
    instr, _ = src.split("\n\n")
    vals = []

    instructions = {}
    for inst in instr.splitlines():
        name, comp = inst[:-1].split("{")
        comps = []
        for c in comp.split(","):
            if ":" not in c:
                comps.append((None, None, None, c))
                continue
            cond,ne = c.split(":")
            var = cond[0]
            op = cond[1]
            v = int(cond[2:])
            comps.append((var,op,v,ne))
        instructions[name] = comps
    
    process = [("in", {n: (1,4000) for n in "xmas"})]

    s = 0
    while process:
        instr, val = process.pop()
        
        while instr not in ("R", "A"):
            for var,op,v,ne in instructions[instr]:
                if var is None:
                    instr = ne
                elif op == "<":
                    if val[var][1] < v:
                        instr = ne
                        break
                    elif val[var][0] < v:
                        nval = {k:v for k,v in val.items()}
                        nval[var] = (val[var][0], v-1)
                        process.append((ne, nval))

                        val[var] = (v, val[var][1])
                elif op == ">":
                    if val[var][0] > v:
                        instr = ne
                        break
                    elif val[var][1] > v:
                        nval = {k:v for k,v in val.items()}
                        nval[var] = (v+1, val[var][1])
                        process.append((ne, nval))

                        val[var] = (val[var][0], v)
        if instr == "A":
            s += reduce(lambda x,y: x*y, (b-a+1 for a,b in val.values()))
    return s
