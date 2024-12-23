import sys
from collections import defaultdict
from itertools import combinations

adj = defaultdict(set)

for line in sys.stdin.readlines():
    a, b = line.strip().split("-")
    adj[a].add(b)
    adj[b].add(a)

triplets = set()
for x in adj.keys():
    for y,z in combinations(adj[x], 2):
        if z in adj[y]:
            if x[0] == "t" or y[0] == "t" or z[0] == "t":
                triplets.add(frozenset((x, y, z)))
print(len(triplets))
# print(triplets)
