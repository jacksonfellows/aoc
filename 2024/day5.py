import sys

rules_mode = True

rules = []
updates = []

for line in sys.stdin.readlines():
    if line == "\n":
        rules_mode = False
        continue
    if rules_mode:
        rules.append([int(x) for x in line.split("|")])
    else:
        updates.append([int(x) for x in line.split(",")])

def is_valid(pages):
    for a,b in rules:
        if a in pages and b in pages:
            if pages.index(a) > pages.index(b):
                return False
    return True

def fix(pages):
    dirty = True
    while dirty:
        dirty = False
        for a,b in rules:
            if a in pages and b in pages:
                i, j = pages.index(a), pages.index(b)
                if i > j:
                    pages[i], pages[j] = pages[j], pages[i]
                    dirty = True

A = B = 0
for pages in updates:
    if is_valid(pages):
        A += pages[len(pages)//2]
    else:
        fix(pages)
        B += pages[len(pages)//2]

print("A", A, "B", B)
