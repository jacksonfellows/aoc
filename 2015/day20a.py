import sys

def n_presents(house):
    np = 0
    for i in range(1, house+1):
        if house%i==0: np += 10*i
    return np

# print([(h,n_presents(h)) for h in range(1,10)])

houses = [1]

for _ in range(200):
    for h in houses[:2000]:
        if n_presents(h) >= 34000000:
            print(h, n_presents(h))
            sys.exit(0)
    new_houses = set()
    for house in houses[:200]:
        for f in range(2, 200):
            new_houses.add(house*f)
    houses = sorted(new_houses)