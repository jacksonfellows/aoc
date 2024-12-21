import sys
from collections import Counter, defaultdict
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

def traceback(came_from, x):
    trace = []
    while x != start:
        trace.append(x)
        x = came_from[x]
    trace.append(start)
    return trace

def search():
    open_set = set([start])
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    came_from = {}
    while len(open_set) > 0:
        current = min(open_set, key=lambda x: g_score[x])
        if current[0] == end[0] and current[1] == end[1]:
            return g_score[current], traceback(came_from, current)
        open_set.remove(current)
        for neighbor in neighbors(current):
            ten_g_score = g_score[current] + 1
            if ten_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = ten_g_score
                open_set.add(neighbor)

no_cheat_time, trace = search()

def dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

N = 0
for i in range(len(trace)):
    for j in range(i+1, len(trace)):
        d = dist(trace[i], trace[j])
        if d <= 20:
            saved = j - i - d
            if saved >= 100:
                N += 1
print(N)
