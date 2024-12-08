import sys
from collections import defaultdict
from itertools import combinations_with_replacement

P = defaultdict(list)
for r,line in enumerate(sys.stdin.readlines()):
    for c,x in enumerate(line.strip()):
        if x.isdigit() or x.isalpha():
            P[x].append(c+r*1j)

r += 1
c += 1
print(f"{r}x{c}")

# map = []
# for _ in range(r+1): map.append(["."]*(c+1))

S = set()
for antennas in P.values():
    for a,b in combinations_with_replacement(antennas, r=2):
        if a != b:
            d = a - b
            for n in (a+d, b-d):
                if 0 <= n.real < c and 0 <= n.imag < r:
                    # map[int(n.imag)][int(n.real)] = "#"
                    S.add(n)
print(len(S))

# print("\n".join("".join(x) for x in map))
