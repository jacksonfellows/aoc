import itertools
import re
import sys

import numpy as np


def find_cost(A, m, b):
    x = np.round(np.linalg.inv(A)@b).astype("int")
    if np.all(A@x - b == 0):
        return 3*x[0] + x[1]
    return 0

part_a_cost = part_b_cost = 0
for lines in itertools.batched(sys.stdin.readlines(), 4):
    r = re.compile("X\\+([0-9]+), Y\\+([0-9]+)")
    Am, Bm = r.search(lines[0]), r.search(lines[1])
    A = np.array(((int(Am[1]), int(Bm[1])), (int(Am[2]), int(Bm[2]))))
    m = re.search("X=([0-9]+), Y=([0-9]+)", lines[2])
    b = np.array((int(m[1]), int(m[2])))
    part_a_cost += find_cost(A, m, b)
    part_b_cost += find_cost(A, m, b+10000000000000)

print(part_a_cost, part_b_cost)
