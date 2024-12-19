import re
import sys


def make_regexp(l):
    return re.compile("^(?:"+"|".join(l)+")*$")

towels = sys.stdin.readline().strip().split(", ")
dirty = True
while dirty:
    dirty = False
    for i in range(len(towels)):
        towel = towels[i]
        rest = towels[:i] + towels[i+1:]
        if make_regexp(rest).match(towel):
            towels = rest
            dirty = True
            break

r = make_regexp(towels)

sys.stdin.readline()
C = 0
for line in sys.stdin.readlines():
    if r.match(line.strip()):
        C += 1
print(C)
