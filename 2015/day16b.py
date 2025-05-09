import sys
import re

r = re.compile("^Sue ([0-9]+): (.+)")
for line in sys.stdin.readlines():
    m = r.match(line)
    n = int(m[1])
    found = [x.split(": ") for x in m[2].split(", ")]
    found = {x[0]:int(x[1]) for x in found}
    if ("children" not in found or found["children"]==3) and ("cats" not in found or found["cats"]>7) and ("samoyeds" not in found or found["samoyeds"]==2) and ("pomeranians" not in found or found["pomeranians"]<3) and ("akitas" not in found or found["akitas"]==0) and ("vizslas" not in found or found["vizslas"]==0) and ("goldfish" not in found or found["goldfish"]<5) and ("trees" not in found or found["trees"]>3) and ("cars" not in found or found["cars"]==2) and ("perfumes" not in found or found["perfumes"]==1): print(n)
