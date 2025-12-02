import sys

dial = 50
n0 = 0
for line in sys.stdin.readlines():
    line = line.strip()
    n = {"L":-1,"R":1}[line[0]]*int(line[1:])
    dial = (dial + n)%100
    if dial == 0: n0 += 1
print(n0)
