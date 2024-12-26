import itertools
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

def get_int(letter, v):
    n = 0
    for wire,bit in v.items():
        if wire[0] == letter:
            pos = int(wire[1:])
            n |= (bit << pos)
    return n

def set_int(letter, n, v):
    for pos in range(45):
        v[f"{letter}{pos:02}"] = n & 1
        n = n >> 1

def run(vals_, ops_):
    dirty = True
    while dirty:
        dirty = False
        ops__ = ops_.copy()
        for dst,(op,x,y) in ops__.items():
            if x in vals_ and y in vals_:
                vals_[dst] = dict(AND=iand, OR=ior, XOR=ixor)[op](vals_[x], vals_[y])
                del ops_[dst]
                dirty = True
    return vals_, ops_

def find_highest_bit_dep(wire):
    if wire in ops:
        _, x, y = ops[wire]
        return max(find_highest_bit_dep(x), find_highest_bit_dep(y))
    if wire[0] in "xy":
        return int(wire[1:])

highest_bit = {}
for wire in ops.keys():
    highest_bit[wire] = find_highest_bit_dep(wire)

def check(x, y, swaps):
    vals_, ops_ = vals.copy(), ops.copy()
    set_int("x", x, vals_)
    set_int("y", y, vals_)
    for a,b in swaps:
        ops_[a], ops_[b] = ops[b], ops[a]
    run(vals_, ops_)
    z = get_int("z", vals_)
    return z == x+y

def check_under(max_pos, swaps):
    for pos in range(max_pos+1):
        if (not check(1<<pos, 0, swaps)) or (not check(0, 1<<pos, swaps)) or (not check(1<<pos, 1<<pos, swaps)) or (not check((1<<pos)-1, 12, swaps)):
            return False
    return True

possible_swaps = [()]

for pos in range(44):
    x = 1<<pos
    y = 0
    vals_, ops_ = vals.copy(), ops.copy()
    set_int("x", x, vals_)
    set_int("y", y, vals_)
    run(vals_, ops_)
    z = get_int("z", vals_)
    if z != x+y:
        bads = [w for w in ops.keys() if highest_bit[w] == pos]
        new_swaps = itertools.combinations(bads, 2)
        new_possible_swaps = []
        for swaps in possible_swaps:
            for new_swap in new_swaps:
                new_swap = tuple(sorted(new_swap))
                if check_under(pos, (*swaps, new_swap)):
                    new_possible_swaps.append((*swaps, new_swap))
        possible_swaps = new_possible_swaps

possible_swaps = set(possible_swaps)
for swaps in possible_swaps:
    if check_under(44, swaps):
        flat = []
        for a,b in swaps:
            flat.append(a)
            flat.append(b)
        print(",".join(sorted(flat)))
