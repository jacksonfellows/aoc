import sys
S = 0
for i,x in enumerate(sys.stdin.read().strip()):
    S += {"(":1,")":-1}[x]
    if S == -1:
        print(i+1)
        sys.exit(0)
