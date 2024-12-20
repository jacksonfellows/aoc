import sys
from collections import defaultdict
from itertools import product

M = list(map(list, sys.stdin.read().strip().split("\n")))

L = len(M)
assert L == len(M[0])

def neighbors(state):
    r, c = state
    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
        r_, c_ = r + dr, c + dc
        if 0 <= r_ < L and 0 <= c_ < L and M[r_][c_] != "#":
            yield r_, c_

start = end = None
for r,c in product(range(L), range(L)):
    if M[r][c] == "S":
        start = (r, c)
    if M[r][c] == "E":
        end = (r, c)

def search():
    open_set = set([start])
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    while len(open_set) > 0:
        current = min(open_set, key=lambda x: g_score[x])
        if current[0] == end[0] and current[1] == end[1]:
            return g_score[current]
        open_set.remove(current)
        for neighbor in neighbors(current):
            ten_g_score = g_score[current] + 1
            if ten_g_score < g_score[neighbor]:
                g_score[neighbor] = ten_g_score
                open_set.add(neighbor)

no_cheat_time = search()
print(f"{L=}, {no_cheat_time=}")

S = 0
for r,c in product(range(L), range(L)):
    if M[r][c] == "#":
        M[r][c] = "."
        cheat_time = search()
        if no_cheat_time - cheat_time >= 100:
            S += 1
        M[r][c] = "#"
print(S, "cheats save at least 100 picoseconds")
