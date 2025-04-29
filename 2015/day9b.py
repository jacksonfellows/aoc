import sys
import re
import itertools

dists = {}
cities = set()

r = re.compile("^(.+) to (.+) = ([0-9]+)$")
for line in sys.stdin.readlines():
    m = r.match(line)
    a, b, dist = m[1], m[2], int(m[3])
    dists[(a,b)] = dist
    dists[(b,a)] = dist
    cities.add(a)
    cities.add(b)

max_total_dist = 0
for perm in itertools.permutations(cities):
    total_dist = 0
    for i in range(len(perm)-1):
        total_dist += dists[(perm[i],perm[i+1])]
    max_total_dist = max(max_total_dist, total_dist)
print(max_total_dist)
