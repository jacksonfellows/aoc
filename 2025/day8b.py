import sys
from collections import defaultdict, Counter
from math import prod

a = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin.readlines()]

# compute squared distances between boxes
dists = set()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        dist = (a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2 + (a[i][2] - a[j][2])**2
        dists.add((dist, tuple(sorted((i,j)))))
conn_pairs = [x[1] for x in sorted(dists)]

def len_connected(connections):
    in_circuit = set()
    def go(i):
        if i in in_circuit: return
        in_circuit.add(i)
        for j in connections[i]:
            go(j)
    go(list(connections.keys())[0])
    return len(in_circuit)


for n in range(1,len(conn_pairs)+1):
    connections = defaultdict(list)
    for i,j in conn_pairs[:n]:
        connections[i].append(j)
        connections[j].append(i)
    if len_connected(connections) == len(a):
        i,j = conn_pairs[n-1]
        print(a[i][0]*a[j][0])
        break
