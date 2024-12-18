from day18a import *

for line in sys.stdin.readlines():
    x, y = list(map(int, line.strip().split(",")))
    M[y][x] = "#"
    if search() is None:
        print(",".join(map(str, (x, y))))
        break
