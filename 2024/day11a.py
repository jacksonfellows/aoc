import sys

stones = list(map(int,sys.stdin.read().strip().split()))

for _ in range(25):
    next_stones = {}
    i = 0
    j = 0
    while i < len(stones):
        s = str(stones[i])
        if stones[i] == 0:
            next_stones[j] = 1
        elif len(s) % 2 == 0:
            next_stones[j] = int(s[:len(s)//2])
            next_stones[j+1] = int(s[len(s)//2:])
            j += 1
        else:
            next_stones[j] = stones[i]*2024
        i += 1
        j += 1
    stones = next_stones

print(len(stones))
