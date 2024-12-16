import sys
from collections import defaultdict
from itertools import product

map = [list(line) for line in sys.stdin.read().split()]

start = end = None
for r,c in product(range(len(map)), range(len(map[0]))):
    if map[r][c] == "S": start = (r, c, "E")
    if map[r][c] == "E": end = (r, c, None)

def advance(state):
    r, c, dir = state
    return (r + dict(N=-1,S=1,E=0,W=0)[dir], c + dict(N=0,S=0,E=1,W=-1)[dir], dir)

def neighbors(state):
    r, c, dir = state
    # Turn
    for dir_ in dict(N="WE",S="WE",E="NS",W="NS")[dir]:
        if dir_ != dir:
            yield (r, c, dir_), 1000
    # Move
    r_, c_, dir_ = advance(state)
    if map[r_][c_] != "#":
        yield (r_, c_, dir_), 1

def find_visited(came_from, x):
    visited = set(((x[0],x[1]),))
    if x == start: return visited
    f = came_from[x]
    min_cost = min(cost for src,cost in f)
    for src in [src for src,cost in f if cost==min_cost]:
        visited |= find_visited(came_from, src)
    return visited

def search():
    open_set = set([start])
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    came_from = defaultdict(set)
    while len(open_set) > 0:
        current = min(open_set, key=lambda x: g_score[x])
        if current[0] == end[0] and current[1] == end[1]:
            return g_score[current], find_visited(came_from, current)
        open_set.remove(current)
        for neighbor, cost in neighbors(current):
            ten_g_score = g_score[current] + cost
            if ten_g_score <= g_score[neighbor]:
                came_from[neighbor].add((current, ten_g_score))
                g_score[neighbor] = ten_g_score
                open_set.add(neighbor)

score, visited = search()
print(score, len(visited))
for r,c in visited:
    assert map[r][c] in ".SE"
    map[r][c] = "O"
print("\n".join("".join(line) for line in map))
