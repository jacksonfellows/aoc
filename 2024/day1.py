import sys
from collections import Counter

L, R = [], []
for line in sys.stdin.readlines():
    l, r = [int(x) for x in line.split()]
    L.append(l); R.append(r)

# Part A
L, R = sorted(L), sorted(R)
D = 0
for l,r in zip(L,R):
    D += abs(l-r)
print("A", D)

# Part B
C = Counter()
for r in R: C[r] += 1
S = 0
for l in L:
    S += l*C[l]
print("B", S)
