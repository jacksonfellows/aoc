import sys

pos1 = (0,0)
pos2 = (0,0)
visited = {}

visited[pos1] = True

for i,move in enumerate(sys.stdin.read().strip()):
    if i%2 == 0:
        pos1 = (pos1[0]+{">":1,"<":-1,"^":0,"v":0}[move], pos1[1]+{">":0,"<":0,"^":1,"v":-1}[move])
        visited[pos1] = True
    else:
        pos2 = (pos2[0]+{">":1,"<":-1,"^":0,"v":0}[move], pos2[1]+{">":0,"<":0,"^":1,"v":-1}[move])
        visited[pos2] = True

print(len(visited))
