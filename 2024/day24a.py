import re
import sys
from operator import iand, ior, ixor

r = re.compile("([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)")

vals = {}
ops = {}

m = True
for line in sys.stdin.readlines():
    if line == "\n":
        m = False
    else:
        if m:
            wire, val = line.strip().split(": ")
            vals[wire] = int(val)
        else:
            match = r.search(line)
            ops[match[4]] = (match[2], match[1], match[3])

# print(vals)

dirty = True
while dirty:
    dirty = False
    ops_ = ops.copy()
    for dst,(op,x,y) in ops_.items():
        if x in vals and y in vals:
            vals[dst] = dict(AND=iand, OR=ior, XOR=ixor)[op](vals[x], vals[y])
            del ops[dst]
            dirty = True

# print(vals)

z = 0
for wire,bit in vals.items():
    if wire[0] == "z":
        n = int(wire[1:])
        z = z | (bit << n)
print(z)
print(bin(z))
