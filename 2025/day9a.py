import sys

coords = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin.readlines()]
max_area = 0
for i in range(len(coords)):
    for j in range(i, len(coords)):
        area = (abs(coords[i][0] - coords[j][0]) + 1)*(abs(coords[i][1] - coords[j][1]) + 1)
        max_area = max(area, max_area)
print(max_area)
