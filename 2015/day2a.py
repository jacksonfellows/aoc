import sys
A = 0
for line in sys.stdin.readlines():
    a, b, c = sorted(map(int, line.split("x")))
    A += 3*a*b + 2*a*c + 2*b*c
print(A)
