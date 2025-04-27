import sys
A = 0
for line in sys.stdin.readlines():
    a, b, c = sorted(map(int, line.split("x")))
    A += 2*a+2*b+a*b*c
print(A)
