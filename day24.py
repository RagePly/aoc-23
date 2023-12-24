# x1 + a * vx1 = x2 + b * vx2
# a = (x2 - x1 + b * vx2) / vx1
# y1 + a * vy1 = y2 + b * vy2
# y1 + (x2 - x1 + b * vx2) vy1 / vx1 = y2 + b * vy2
# y1 - y2 + (x2-x1) * vy1 / vx1 + b*vx2 * vy1/vx1 = b * vy2
# b = (y1 - y2 + (x2-x1) * vy1 / vx1) / (vy2 - vx2*vy1/vx1)

def part1(src):
    paths = [list(map(lambda x: list(map(int, x.split(", "))), line.split(" @ "))) for line in src.splitlines()]
    s = 0
    least, most = 200000000000000,400000000000000
    for i,j in [(i,j) for i in range(len(paths)-1) for j in range(i+1,len(paths))]:
        (x1,y1,z1), (vx1,vy1,vz1) = paths[i]
        (x2,y2,z2), (vx2,vy2,vz2) = paths[j]

        try:
            b = (y1 - y2 + (x2-x1) * vy1 / vx1) / (vy2 - vx2*vy1/vx1)
            a = (x2 - x1 + b * vx2) / vx1
        except:
            continue
        
        if b < 0 or a < 0:
            continue

        ix = x + a*vx
        iy = y + a*vy
        
        if ix >= least and ix <= most and iy >= least and iy <= most:
            s += 1
    return s

from sympy import symbols, nonlinsolve
def part2(src):
    paths = [map(lambda x: map(int, x.split(", ")), line.split(" @ ")) for line in src.splitlines()]
    system_t = symbols('t_0, t_1, t_2, t_3')
    system_x = symbols('x,y,z')
    system_d = symbols('dx,dy,dz')
    system = system_t + system_x + system_d

    equations = [
        x - p + t*(d - v)
        for t, [pos,vel] in zip(system_t, paths[:4])
        for x,d,p,v in zip(system_x, system_d, pos, vel)
    ]
    
    [(_,_,_,_, x,y,z, _,_,_)] = nonlinsolve(equations,system)
    return int(x + y + z)
