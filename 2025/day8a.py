import sys
from collections import defaultdict, Counter
from math import prod

a = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin.readlines()]

# compute squared distances between boxes
dists = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        dist = (a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2 + (a[i][2] - a[j][2])**2
        dists.append((dist, sorted((i,j))))

# connect n closest boxes
n = 1000
conn_pairs = [x[1] for x in sorted(dists)][:n]
connections = defaultdict(list)
for i,j in conn_pairs:
    connections[i].append(j)
    connections[j].append(i)


# compute circuits
circuit_ids = {}
ci = 0

def create_circuit(i):
    if i in circuit_ids:
        return
    circuit_ids[i] = ci
    for j in connections[i]:
        create_circuit(j)

for i in range(len(a)):
    if i in circuit_ids.keys():
        continue
    else:
        # create circuit
        create_circuit(i)
        ci += 1

# count how many boxes are in each circuit
circuit_id_counts = Counter()
for ci in circuit_ids.values():
    circuit_id_counts[ci] += 1
print(prod(x[1] for x in circuit_id_counts.most_common(3)))
