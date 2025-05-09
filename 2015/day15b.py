import sys
import re
from math import prod

r = re.compile("^(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)$")
ingred = []
calories = []
for line in sys.stdin.readlines():
    m = r.match(line)
    ingred.append([int(m[i]) for i in range(2,6)])
    calories.append(int(m[6]))

assert len(ingred)==4
max_score = 0
for a in range(101):
    for b in range(100-a+1):
        for c in range(100-(a+b)+1):
            d = 100 - a - b - c
            if sum(x*y for x,y in zip([a,b,c,d],calories)) != 500: continue
            max_score = max(max_score,prod(max(0, sum(amount*ingred[j][i] for j,amount in enumerate([a,b,c,d]))) for i in range(4)))
print(max_score)