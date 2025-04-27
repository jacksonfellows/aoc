import sys
import re

lights = {}

r = re.compile("^(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$")

for line in sys.stdin.readlines():
    m = r.match(line)
    x1, y1, x2, y2 = [int(m[o]) for o in [2,3,4,5]]
    assert 0 <= x1 < 1000 and 0 <= x1 < 1000 and 0 <= y1 < 1000 and 0 <= y2 < 1000
    assert x1 <= x2 and y1 <= y2
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if m[1] == "turn on":
                lights[(x,y)] = 1
            elif m[1] == "turn off":
                lights[(x,y)] = 0
            elif m[1] == "toggle":
                lights[(x,y)] = int(not lights.get((x,y),0))

print(sum(lights.values()))
