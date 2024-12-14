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

def calc_map(i):
    map = np.zeros((dim[1],dim[0]))
    for p, v in zip(ps, vs):
        x,y = (p + i*v) % dim
        map[y][x] += 1
    return map

N = 10_000
sym_scores = np.zeros(N)
for i in range(N):
    map = calc_map(i)
    sym_scores[i] = np.sum(map*map[:,::-1])

i = sym_scores.argmax()
plt.title(i)
plt.imshow(calc_map(i))
plt.show()
