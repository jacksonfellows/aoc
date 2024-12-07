import itertools
import sys
from operator import add, mul


def concat(a, b):
    t = b
    n = 0
    while t > 0:
        t //= 10
        n += 1
    return a*(10**n) + b

S = 0
for line in sys.stdin.readlines():
    val, rest = line.split(": ")
    val = int(val)
    args = list(map(int, rest.split()))
    for ops in itertools.product([add, mul, concat], repeat=len(args)-1):
        res = args[0]
        for i in range(len(args)-1):
            res = ops[i](res, args[i+1])
        if res == val:
            S += val
            break
print(S)
