import sys

s = list(map(int,sys.stdin.read().strip()))

i = 0
j = len(s)-1

checksum = 0
n = 0
while i <= j:
    # ith block
    for _ in range(s[i]):
        checksum += (i//2)*n
        n += 1
    if i == j:
        break
    # Fill space after ith block
    while s[i+1] > 0:
        checksum += (j//2)*n
        n += 1
        s[j] -= 1
        s[i+1] -= 1
        if s[j] == 0:
            j -= 2
    i += 2
print(checksum)
