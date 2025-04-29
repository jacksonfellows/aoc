import sys

n = sys.stdin.read().strip()

for _ in range(40):
    new_n = ""
    i = 0
    while i < len(n):
        j = i + 1
        while j < len(n) and n[i] == n[j]: j += 1
        new_n = new_n + str(j - i) + n[i]
        i = j
    n = new_n
    print(len(n))
