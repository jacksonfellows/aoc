import sys
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation, colors

L = 71
M = np.zeros((L,L))

def neighbors(state):
    r, c = state
    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
        r_, c_ = r + dr, c + dc
        if 0 <= r_ < L and 0 <= c_ < L and M[r_,c_] == 0:
            yield r_, c_

start = (0, 0)
end = (L-1, L-1)

def trace_back(came_from, x):
    visited = []
    while x != start:
        visited.append(x)
        x = came_from[x]
    visited.append(start)
    return visited

def search():
    open_set = set([start])
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    came_from = {}
    while len(open_set) > 0:
        current = min(open_set, key=lambda x: g_score[x])
        if current[0] == end[0] and current[1] == end[1]:
            return g_score[current], trace_back(came_from, current)
        open_set.remove(current)
        for neighbor in neighbors(current):
            ten_g_score = g_score[current] + 1
            if ten_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = ten_g_score
                open_set.add(neighbor)


fig, ax = plt.subplots()
cmap = colors.ListedColormap([(219/255, 237/255, 242/255), "black", (248/255, 225/255, 75/255)])
ax.imshow(M, cmap=cmap)
ax.set_axis_off()
ax.set_aspect("equal")

ims = []
for line in sys.stdin.readlines():
    x, y = list(map(int, line.strip().split(",")))
    M[y,x] = 1
    S = search()
    if S is None: break
    cost, visited = S
    I = M.copy()
    for r,c in visited:
        I[r,c] = 2
    im = ax.imshow(I, cmap=cmap)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, blit=True, repeat=False)
writer = animation.FFMpegWriter(fps=60)
ani.save("day18b.mp4", writer=writer)
