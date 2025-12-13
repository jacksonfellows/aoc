import sys
from itertools import product

g = [list(x.strip()) for x in sys.stdin.readlines()]

N = 0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] != "@": continue
        n = 0
        for di,dj in product((-1,0,1), (-1,0,1)):
            if (not ((di==0) and (dj==0))) and 0 <= i+di < len(g) and 0 <= j+dj < len(g[0]):
                if g[i+di][j+dj] == "@":
                    n += 1
        if n < 4:
            N += 1
print(N)
