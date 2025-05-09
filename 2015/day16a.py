import sys
import re

known = [x.split(": ") for x in """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
""".strip().split("\n")]
known = {x[0]:x[1] for x in known}

r = re.compile("^Sue ([0-9]+): (.+)")
for line in sys.stdin.readlines():
    m = r.match(line)
    n = int(m[1])
    if all(known[k]==v for k,v in [x.split(": ") for x in m[2].split(", ")]): print(n)