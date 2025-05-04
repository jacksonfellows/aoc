import sys
import re
from math import floor

r = re.compile("^(.+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.$")

T = 2503

max_dist = 0

for line in sys.stdin.readlines():
    m = r.match(line)
    name, fly_speed, fly_time, rest_time = m[1], int(m[2]), int(m[3]), int(m[4])
    num_cyles = floor(T/(fly_time+rest_time))
    rem_time = T - num_cyles*(fly_time+rest_time)
    dist = num_cyles*fly_speed*fly_time + min(fly_time,rem_time)*fly_speed
    print(name, dist)
    max_dist = max(max_dist,dist)

print(max_dist)
