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
        row = []
        for c in line.strip():
            row.extend({"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}[c])
        map.append(row)

def find_robot():
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "@":
                return r, c

dr = {"^":-1,"v":+1,"<":0,">":0}
dc = {"^":0,"v":0,"<":-1,">":+1}

def find_pushees(r, c, dir):
    if map[r][c] == "#":
        return None
    if map[r][c] == ".":
        return []

    ps = [(r,c)]

    if dir in "^v":
        if map[r][c] == "[" and map[r][c+1] == "]": ps.append((r,c+1))
        if map[r][c] == "]" and map[r][c-1] == "[": ps.append((r,c-1))

    res = []
    for r,c in ps:
        rec = find_pushees(r+dr[dir], c+dc[dir], dir)
        if rec is None: return None
        else:
            res.extend(rec)
    res.extend(ps)
    return res

def do_move(dir):
    rr, cc = find_robot()
    ps = find_pushees(rr, cc, dir)
    if ps is not None:
        for i,(r,c) in enumerate(ps):
            if (r,c) not in ps[:i]: # Don't do moves twice!!
                map[r+dr[dir]][c+dc[dir]] = map[r][c]
                map[r][c] = "."

# print("initial state:")
# print_map()
# print()

for move in moves:
    do_move(move)
    # print("move:", move)
    # print_map()
    # print()

# print_map()

score = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == "[":
            score += 100*r + c
print(score)
