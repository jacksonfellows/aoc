import sys
from itertools import count

total_joltage = 0
for line in sys.stdin.readlines():
    digits = [int(x) for x in line.strip()]
    d1,i = max(zip(digits[:-1], count()), key=lambda x:x[0])
    d2 = max(digits[i+1:])
    total_joltage += 10*d1 + d2
print(total_joltage)
