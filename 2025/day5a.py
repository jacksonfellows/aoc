import sys

ranges = []
n_fresh = 0
range_mode = True

for line in sys.stdin.readlines():
    if len(line.strip())==0:
        range_mode = False
        continue
    if range_mode:
        ranges.append([int(x) for x in line.split("-")])
    else:
        n = int(line)
        for (lo,hi) in ranges:
            if lo <= n <= hi:
                n_fresh += 1
                break

print(n_fresh)
