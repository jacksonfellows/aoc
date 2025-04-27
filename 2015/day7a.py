import sys
from numpy import uint16

circuit = {}

for line in sys.stdin.readlines():
    l, r = line.split(" -> ")
    l = [x if x.isalpha() else uint16(x) for x in l.split(" ")]
    if len(l) == 3: l = [l[1],l[0],l[2]]
    circuit[r.strip()] = l

ops = {"NOT": lambda x: ~x, "AND": lambda x,y: x&y, "OR": lambda x,y: x|y, "LSHIFT": lambda x,y: x<<y, "RSHIFT": lambda x,y: x>>y}

wires = {}

dirty = True
while dirty:
    dirty = False
    circuit_copy = circuit.copy()
    for wire,expr in circuit_copy.items():
        if len(expr) == 1:
            if type(expr[0]) == uint16:
                wires[wire] = expr[0]
                del circuit[wire]
                dirty = True
            if expr[0] in wires:
                wires[wire] = wires[expr[0]]
                del circuit[wire]
                dirty = True
        else:
            args = [wires[x] if x in wires else x for x in expr[1:]]
            if all(type(x) == uint16 for x in args):
                wires[wire] = ops[expr[0]](*args)
                del circuit[wire]
                dirty = True

print(wires["a"])
