import sys
print(sum({"(":1,")":-1}[x] for x in sys.stdin.read().strip()))
