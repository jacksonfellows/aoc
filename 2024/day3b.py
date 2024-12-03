import re
import sys

S = 0
do = True
for a in re.findall("(mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\))", sys.stdin.read()):
    if a[0].startswith("mul"):
        if do:
            S += int(a[1])*int(a[2])
    elif a[0] == "do()":
        do = True
    elif a[0] == "don't()":
        do = False
    else:
        print(a)
        assert 0
print(S)
