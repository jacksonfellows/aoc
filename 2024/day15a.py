import sys

map = []
m = False
moves = []

def print_map():
    print("\n".join("".join(line) for line in map))

for line in sys.stdin.readlines():
    if line == "\n":
        m = True
    if m:
        moves.extend(list(line.strip()))
    else:
        map.append(list(line.strip()))

def find_robot():
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "@":
                return r, c

def shift_dir(r, c, dir):
    dr = {"^":-1,"v":+1,"<":0,">":0}
    dc = {"^":0,"v":0,"<":-1,">":+1}
    return r + dr[dir], c + dc[dir]

def push(r, c, dir):
    if map[r][c] == "#": return False
    if map[r][c] == ".": return True
    r_, c_ = shift_dir(r, c, dir)
    if push(r_, c_, dir):
        map[r_][c_] = map[r][c]
        return True

def do_move(move):
    r, c = find_robot()
    if push(r, c, move):
        map[r][c] = "."

for move in moves:
    do_move(move)

print_map()

score = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == "O":
            score += 100*r + c
print(score)
