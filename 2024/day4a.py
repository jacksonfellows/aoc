import sys

S = "XMAS"

rows = sys.stdin.read().strip().split("\n")
cols = ["".join(rows[i][j] for i in range(len(rows))) for j in range(len(rows[0]))]
diags1 = ["".join(rows[o+i][i] for i in range(min(len(rows[0]), len(rows) - o))) for o in range(len(rows))]
diags2 = ["".join(rows[i][o+i] for i in range(min(len(rows), len(rows[0]) - o))) for o in range(1, len(rows))]
diags3 = ["".join(rows[o+i][-(i+1)] for i in range(min(len(rows[0]), len(rows) - o))) for o in range(len(rows))]
diags4 = ["".join(rows[i][-(o+i+1)] for i in range(min(len(rows), len(rows[0]) - o))) for o in range(1, len(rows))]

count_matches = lambda str: sum(str[i:i+4] in (S,S[::-1]) for i in range(len(str)))

print(sum(count_matches(s) for s in rows + cols + diags1 + diags2 + diags3 + diags4))
