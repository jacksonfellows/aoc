import sys

import numpy as np

N = 0
for line in sys.stdin.readlines():
    level = np.array([int(x) for x in line.split()])
    diffs = level[1:] - level[:-1]
    if (np.all(diffs > 0) or np.all(diffs < 0)) and np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3):
        N += 1

print(N)
