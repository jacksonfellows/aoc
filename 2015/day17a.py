import sys
from functools import cache

all_containers = tuple(sorted([int(x.strip()) for x in sys.stdin.readlines()]))

@cache
def n_ways(total, containers):
    if total == 0: return 1
    s = 0
    for i in range(len(containers)):
        if containers[i] > total: break
        if containers[i] == total:
            s += 1
        else:
            s += n_ways(total-containers[i], containers[i+1:])
    return s

print(n_ways(150, all_containers))