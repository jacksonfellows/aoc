import sys


def works(target, args):
    # "Work backward": idea from post on AOC reddit.
    if len(args) == 1:
        return target == args[0]
    x = args[-1]
    rem = args[:-1]
    # +
    if works(target - x, rem):
        return True
    # *
    if target % x == 0 and works(target // x, rem):
        return True
    # ||
    if str(target).endswith(str(x)) and len(str(target)) > len(str(x)) and works(int(str(target)[:-len(str(x))]), rem):
        return True
    return False

S = 0
for line in sys.stdin.readlines():
    val, rest = line.split(": ")
    val = int(val)
    args = list(map(int, rest.split()))
    if works(val, args):
        S += val
print(S)
