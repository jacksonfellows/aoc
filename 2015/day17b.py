import sys
from functools import cache

all_containers = tuple(sorted([int(x.strip()) for x in sys.stdin.readlines()]))

@cache
def n_ways(total, containers, n_used):
    if total == 0: return 1
    s = 0
    for i in range(len(containers)):
        if containers[i] > total: break
        if containers[i] == total:
            if n_used == 3: s += 1 # guess-and-check to find n_used==3 (really 4 used)
        else:
            s += n_ways(total-containers[i], containers[i+1:], n_used+1)
    return s

print(n_ways(150, all_containers, 0))