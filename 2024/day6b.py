import sys

map = [list(line) for line in sys.stdin.read().split()]

def find_start():
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "^":
                return r, c

def does_loop(r, c, dir):
    states = set()
    while (0 <= r < len(map)) and (0 <= c < len(map[0])):
        if (r,c,*dir) in states:
            return True
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
            states.add((r,c,*dir))
            r += dir[0]
            c += dir[1]
    return False

start_r, start_c = find_start()
dir = (-1, 0)

print(len(map), len(map[0]))

L = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == ".":
            map[r][c] = "#"
            L += does_loop(start_r, start_c, dir)
            map[r][c] = "."
print(L)
