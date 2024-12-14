import re
import sys

import numpy as np

dim = np.array((101, 103))
quad_counts = np.zeros(4, dtype="int")

for line in sys.stdin.readlines():
    m = re.search("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)
    p = np.array((int(m[1]),int(m[2])))
    v = np.array((int(m[3]),int(m[4])))
    x,y = (p + 100*v) % dim
    if x < dim[0]//2 and y < dim[1]//2: quad_counts[0] += 1
    if x < dim[0]//2 and y > dim[1]//2: quad_counts[1] += 1
    if x > dim[0]//2 and y > dim[1]//2: quad_counts[2] += 1
    if x > dim[0]//2 and y < dim[1]//2: quad_counts[3] += 1

print(np.prod(quad_counts))
