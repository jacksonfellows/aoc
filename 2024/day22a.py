import sys


def next_secret_number(x):
    x = (x^(x*64))%16777216
    x = (x^(x//32))%16777216
    x = (x^(x*2048))%16777216
    return x

S = 0
for line in sys.stdin.readlines():
    x = int(line.strip())
    for _ in range(2000):
        x = next_secret_number(x)
    S += x
print(S)
