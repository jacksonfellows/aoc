import sys
from math import prod

a = [list(line.split()) for line in sys.stdin.readlines()]
ops = a[-1]
A = [[int(x) for x in row] for row in a[:-1]]

total = 0
for j,op in enumerate(ops):
    if op == "+": total += sum(row[j] for row in A)
    elif op == "*": total += prod(row[j] for row in A)
    else: assert 0
print(total)
