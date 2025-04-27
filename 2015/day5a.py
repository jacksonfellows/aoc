import sys

def nice(s):
    if sum(x in "aeiou" for x in s) < 3: return False
    if not any(x == y for x,y in zip(s[:-1], s[1:])): return False
    if any(x in s for x in ["ab","cd","pq","xy"]): return False
    return True

C = 0
for line in sys.stdin.readlines():
    C += nice(line.strip())
print(C)
