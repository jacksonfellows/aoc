import sys
from itertools import count

total_joltage = 0
for line in sys.stdin.readlines():
    digits = [int(x) for x in line.strip()]
    joltage = 0
    for i in range(12):
        d,j = max(zip(digits[:len(digits)-(11-i)], count()), key=lambda x: x[0])
        joltage = 10*joltage + d
        digits = digits[j+1:]
    total_joltage += joltage
print(total_joltage)
