import sys
from itertools import product


def pin_heights(board):
    heights = [0,0,0,0,0]
    for i in range(1, len(board)):
        for j in range(5):
            if board[i][j] == "#":
                heights[j] += 1
    return heights

locks = []
keys = []

for board in sys.stdin.read().split("\n\n"):
    board = board.strip().split("\n")
    if board[0] == "#####":
        locks.append(pin_heights(board))
    elif board[-1] == "#####":
        keys.append(pin_heights(board[::-1]))
    else:
        print(board)
        assert 0

def fits(lock, key):
    for x,y in zip(lock, key):
        if x+y > 5:
            return False
    return True

C = 0
for lock,key in product(locks, keys):
    if fits(lock, key):
        C += 1
print(C)
