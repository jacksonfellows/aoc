import sys

rows = sys.stdin.read().strip().split("\n")

P = ("MAS", "SAM")

C = 0
for r in range(len(rows)-2):
    for c in range(len(rows[0])-2):
        if (rows[r][c]+rows[r+1][c+1]+rows[r+2][c+2]) in P and (rows[r][c+2]+rows[r+1][c+1]+rows[r+2][c]) in P:
            C += 1
print(C)
