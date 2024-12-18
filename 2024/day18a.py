import sys
from collections import defaultdict

L = 71
M = []
for _ in range(L):
    M.append(["."]*L)

def neighbors(state):
    r, c = state
    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
        r_, c_ = r + dr, c + dc
        if 0 <= r_ < L and 0 <= c_ < L and M[r_][c_] == ".":
            yield r_, c_

start = (0, 0)
end = (L-1, L-1)

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

if __name__ == "__main__":
    n_bytes = 1024
    for _ in range(n_bytes):
        line = sys.stdin.readline()
        x, y = list(map(int, line.strip().split(",")))
        M[y][x] = "#"
    print(search())
