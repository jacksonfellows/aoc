import sys
from collections import defaultdict
from functools import cache

lines = sys.stdin.readlines()
rules_ = [line.strip().split(" => ") for line in lines[:-2]]
rules = defaultdict(list)
for r in rules_:
    rules[r[1]].append(r[0])
start = lines[-1].strip()

@cache
def find_e(mol, n):
    if mol == "e": return n
    children = set()
    for i in range(len(mol)):
        for offset in range(1,10):
            if mol[i:i+offset] in rules:
                for rep in rules[mol[i:i+offset]]:
                    children.add(mol[:i] + rep + mol[i+offset:])
    for child in sorted(children, key=len):
        n_ = find_e(child, n+1)
        if n_ is not None: return n_
    return None

print(find_e(start, 0))
