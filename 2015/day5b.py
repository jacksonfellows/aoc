import sys

def nice(s):
    pair = False
    repeat = False
    for i in range(0, len(s)-2):
        if s[i:i+2] in s[i+2:]: pair = True
        if s[i] == s[i+2]: repeat = True
    return pair and repeat

C = 0
for line in sys.stdin.readlines():
    C += nice(line.strip())
print(C)
