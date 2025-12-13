import sys

ranges = []
for line in sys.stdin.readlines():
    if len(line.strip()) == 0: break
    lo, hi = [int(x) for x in line.split("-")]
    assert lo <= hi
    ranges.append((lo, hi))

ranges = list(sorted(ranges))

i = 0
while i < len(ranges):
    while i+1 < len(ranges) and ranges[i][1] >= ranges[i+1][0]:
        ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[i+1][1]))
        del ranges[i+1]
    i += 1

print(sum(hi - lo + 1 for lo,hi in ranges))
