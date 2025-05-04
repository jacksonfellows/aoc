import sys
import re
from math import floor
from collections import defaultdict

r = re.compile("^(.+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.$")

T = 2503

rinfo, rdist = {}, {}
for line in sys.stdin.readlines():
    m = r.match(line)
    name, fly_speed, fly_time, rest_time = m[1], int(m[2]), int(m[3]), int(m[4])
    rinfo[name] = (fly_speed, fly_time, rest_time)
    rdist[name] = 0

rpoints = defaultdict(lambda: 0)
for t in range(T):
    for name,dist in rdist.copy().items():
        fly_speed, fly_time, rest_time = rinfo[name]
        i = t%(fly_time+rest_time)
        if i < fly_time:
            rdist[name] += fly_speed
    max_dist = max(rdist.values())
    for name,dist in rdist.items():
        if dist == max_dist:
            rpoints[name] += 1

print(max(rpoints.values()))
