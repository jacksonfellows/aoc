import sys
from math import prod

lines = sys.stdin.readlines()
rows = lines[:-1]
last = lines[-1].rstrip("\n")

tot = 0
cur_op = None
cols = []
for j in range(len(last)):
    if last[j] != " ": cur_op = last[j]
    col = [row[j] for row in rows]
    if all(x == " " for x in col) or j == len(last)-1:
        if j == len(last)-1: cols.append(col)
        nums = [int("".join(col).strip()) for col in cols]
        res = {"+": sum, "*": prod}[cur_op](nums)
        tot += res
        cols = []
    else:
        cols.append(col)
print(tot)
