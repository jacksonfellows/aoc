import sys

i = sys.stdin.read().strip()
id_sum = 0
for id_range in i.split(","):
    start, stop = [int(x) for x in id_range.split("-")]
    for n in range(start, stop+1):
        s = str(n)
        L = len(s)
        for j in range(1, L//2+1):
            if L%j == 0 and s == s[:j]*(L//j):
                id_sum += n
                break
print(id_sum)
