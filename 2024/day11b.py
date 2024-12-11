import sys
from functools import cache

stones = list(map(int,sys.stdin.read().strip().split()))

@cache
def dfs(x, n):
    if n == 0:
        return 1
    if x == 0:
        return dfs(1, n-1)
    s = str(x)
    if len(s)%2 == 0:
        return dfs(int(s[:len(s)//2]), n-1) + dfs(int(s[len(s)//2:]), n-1)
    return dfs(x*2024, n-1)

print(sum(dfs(x, 75) for x in stones))
