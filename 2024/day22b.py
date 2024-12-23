import sys

import numpy as np


def next_secret_number(x):
    x = (x^(x*64))%16777216
    x = (x^(x//32))%16777216
    x = (x^(x*2048))%16777216
    return x

bananas = np.zeros((19,19,19,19), dtype="int")

def find_bananas(x):
    seen = np.zeros((19,19,19,19), dtype="bool")
    changes = []
    last_price = x%10
    x = next_secret_number(x)
    for _ in range(2000):
        price = x%10
        change = price - last_price
        assert -9 <= change <= 9
        changes.append(change)
        assert len(changes) <= 4
        if len(changes) == 4:
            if not seen[changes[0]+9,changes[1]+9,changes[2]+9,changes[3]+9]:
                bananas[changes[0]+9,changes[1]+9,changes[2]+9,changes[3]+9] += price
                seen[changes[0]+9,changes[1]+9,changes[2]+9,changes[3]+9] = True
            changes = changes[1:]
        x = next_secret_number(x)
        last_price = price

for line in sys.stdin.readlines():
    x = int(line.strip())
    find_bananas(x)
print(np.max(bananas))
# print(tuple(int(x-9) for x in np.unravel_index(np.argmax(bananas), bananas.shape)))
