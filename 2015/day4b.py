import sys
from hashlib import md5

key = sys.stdin.read().strip()

n = 1
while 1:
    digest = md5(bytes(key + str(n), "ascii")).digest()
    if digest[0] == 0 and digest[1] == 0 and digest[2] == 0:
        print(n)
        break
    n += 1
