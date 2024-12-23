import sys
from collections import defaultdict
from itertools import combinations

adj = defaultdict(set)

for line in sys.stdin.readlines():
    a, b = line.strip().split("-")
    adj[a].add(b)
    adj[b].add(a)

party_len = 0
party = None
for x in adj.keys():
    for r in range(2, len(adj[x])+1):
        for rest in combinations(adj[x], r):
            works = True
            for y in rest:
                if not all(z in adj[y] for z in rest if z != y):
                    works = False
                    break
            if works:
                if len(rest) + 1 > party_len:
                    party = set(rest)
                    party.add(x)
                    party_len = len(party)
                    assert party_len == len(rest) + 1
print(",".join(sorted(party)))
