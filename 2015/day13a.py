import sys
import re
import itertools

happy = {}

r = re.compile("^(.+) would (gain|lose) ([0-9]+) happiness units by sitting next to (.+)\\.$")
for line in sys.stdin.readlines():
    m = r.match(line)
    happy[(m[1],m[4])] = {"gain":1,"lose":-1}[m[2]]*int(m[3])

def total_happiness(table):
    tot = 0
    for i in range(len(table)):
        tot += happy[(table[i],table[(i-1)%len(table)])] + happy[(table[i],table[(i+1)%len(table)])]
    return tot

people = set(k[0] for k in happy.keys())
max_happy = 0
for table in itertools.permutations(people):
    max_happy = max(max_happy, total_happiness(table))
print(max_happy)

