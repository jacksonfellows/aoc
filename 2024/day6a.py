import sys

map = [list(line) for line in sys.stdin.read().split()]

def find_start():
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "^":
                return r, c
r, c = find_start()
dir = (-1, 0)

while (0 <= r < len(map)) and (0 <= c < len(map[0])):
    if map[r][c] == "#":
        r -= dir[0]
        c -= dir[1]
        dir = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0)
        }[dir]
    else:
        map[r][c] = "X"
        r += dir[0]
        c += dir[1]

V = 0
for r in range(len(map)):
    for c in range(len(map)):
        if map[r][c] == "X":
            V += 1
print(V)
