import sys

dial = 50
n0 = 0
for line in sys.stdin.readlines():
    line = line.strip()
    n = int(line[1:])
    d = {"L":-1,"R":1}[line[0]]
    for _ in range(n):
        dial += d
        if dial == 100: dial = 0
        if dial == 0: n0 += 1
        if dial == -1: dial = 99
print(n0)
