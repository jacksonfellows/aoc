import sys

i = sys.stdin.read().strip()
id_sum = 0
for id_range in i.split(","):
    start, stop = [int(x) for x in id_range.split("-")]
    for n in range(start, stop+1):
        s = str(n)
        if len(s)%2==0 and s[:len(s)//2] == s[len(s)//2:]:
            id_sum += n
print(id_sum)
