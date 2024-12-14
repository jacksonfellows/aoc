import re
import sys

import numpy as np

dim = np.array((101, 103))

ps, vs = [], []

for line in sys.stdin.readlines():
    m = re.search("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)
    ps.append(np.array((int(m[1]),int(m[2]))))
    vs.append(np.array((int(m[3]),int(m[4]))))

def calc_quad_counts(i):
    q = np.zeros(4, dtype="int")
    for p, v in zip(ps, vs):
        x,y = (p + i*v) % dim
        if x < dim[0]//2 and y < dim[1]//2: q[0] += 1
        if x < dim[0]//2 and y > dim[1]//2: q[1] += 1
        if x > dim[0]//2 and y > dim[1]//2: q[2] += 1
        if x > dim[0]//2 and y < dim[1]//2: q[3] += 1
    return q

if __name__ == "__main__":
    print(np.prod(calc_quad_counts(100)))
