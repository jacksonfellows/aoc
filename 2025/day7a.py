import sys

a = [list(x.strip()) for x in sys.stdin.readlines()]

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == "S":
            start_i, start_j = i, j
            break

a[start_i][start_j] = "|"

splits = 0
for i in range(start_i, len(a)-1):
    for j in range(len(a[0])):
        if a[i][j] == "|":
            if a[i+1][j] == ".":
                assert a[i+1][j] in ".|"
                a[i+1][j] = "|"
            elif a[i+1][j] == "^":
                splits += 1
                assert a[i+1][j-1] in ".|"
                assert a[i+1][j+1] in ".|"
                a[i+1][j-1] = "|"
                a[i+1][j+1] = "|"
            elif a[i+1][j] == "|":
                pass
            else:
                assert 0

print(splits)
