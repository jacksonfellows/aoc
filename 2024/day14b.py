import re
import sys

import matplotlib.pyplot as plt
import numpy as np

dim = np.array((101, 103))

ps, vs = [], []

for line in sys.stdin.readlines():
    m = re.search("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)
    ps.append(np.array((int(m[1]),int(m[2]))))
    vs.append(np.array((int(m[3]),int(m[4]))))

for j in range(100):
    i = 81 + 101*j
    map = np.zeros((dim[1],dim[0]))
    for p, v in zip(ps, vs):
        x,y = (p + i*v) % dim
        map[y][x] += 1
    plt.title(i)
    plt.imshow(map)
    plt.show()
