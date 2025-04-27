import sys

pos = (0,0)
visited = {}

visited[pos] = True

for move in sys.stdin.read().strip():
    pos = (pos[0]+{">":1,"<":-1,"^":0,"v":0}[move], pos[1]+{">":0,"<":0,"^":1,"v":-1}[move])
    visited[pos] = True

print(len(visited))
