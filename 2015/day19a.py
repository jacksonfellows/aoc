import sys
from collections import defaultdict

lines = sys.stdin.readlines()
rules_ = [line.strip().split(" => ") for line in lines[:-2]]
rules = defaultdict(list)
for r in rules_:
    rules[r[0]].append(r[1])
mol = lines[-1]

print(max(map(len,rules.keys())))

mols = set()

for i in range(len(mol)):
    if mol[i] in rules:
        for rep in rules[mol[i]]:
            mols.add(mol[:i] + rep + mol[i+1:])
    if mol[i:i+2] in rules:
        for rep in rules[mol[i:i+2]]:
            mols.add(mol[:i] + rep + mol[i+2:])

print(len(mols))
