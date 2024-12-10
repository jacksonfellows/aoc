import sys

map = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

def adj(state):
    r,c = state
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        r_,c_ = r+dr,c+dc
        if 0 <= r_ < len(map) and 0 <= c_ < len(map[0]) and map[r_][c_] == map[r][c]+1:
            yield r_,c_

def dfs(state):
    A = list(adj(state))
    if len(A) == 0:
        yield state
    else:
        for a in A:
            yield from dfs(a)

score = 0
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 0:
            for r_,c_ in dfs((r,c)):
                if map[r_][c_] == 9:
                    score += 1
print(score)
