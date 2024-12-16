import sys
from collections import defaultdict
from itertools import product

from day16a import end, map, neighbors, start


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
