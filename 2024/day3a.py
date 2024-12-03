import re
import sys

S = 0
for x,y in re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", sys.stdin.read()):
    S += int(x)*int(y)
print(S)
