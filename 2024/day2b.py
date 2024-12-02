import sys

import numpy as np


def safe(level):
    diffs = level[1:] - level[:-1]
    return (np.all(diffs > 0) or np.all(diffs < 0)) and np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3)

N = 0
for line in sys.stdin.readlines():
    level = np.array([int(x) for x in line.split()])
    if safe(level):
        N += 1
    else:
        for i in range(len(level)):
            if safe(np.concatenate((level[:i], level[i+1:]))):
                N += 1
                break

print(N)
