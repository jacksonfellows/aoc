import sys
from functools import cache

towels = sys.stdin.readline().strip().split(", ")

@cache
def n_ways(design):
    if len(design) == 0: return 1
    ways = 0
    for towel in towels:
        if design.startswith(towel):
            ways += n_ways(design[len(towel):])
    return ways

sys.stdin.readline()
P = 0
for line in sys.stdin.readlines():
    P += n_ways(line.strip())
print(P)
