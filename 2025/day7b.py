import sys
import itertools
from collections import Counter

a = [list(x.strip()) for x in sys.stdin.readlines()]

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == "S":
            start_i, start_j = i, j
            break

ways = {(start_j,): 1}

for i in range(start_i, len(a)-1):
    new_ways = Counter()
    for js, n in ways.items():
        # TODO make list of possible new j indices in next row, then use that to update new_ways
        new_js = []
        for j in js:
            if a[i+1][j] == ".":
                new_js.append((j,))
            elif a[i+1][j] == "^":
                new_js.append((j-1,j+1))
            else:
                assert 0
        for js in itertools.product(*new_js):
            new_ways[js] += n
    ways = new_ways

print(sum(ways.values()))
