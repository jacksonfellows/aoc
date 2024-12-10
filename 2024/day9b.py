import sys

s = list(map(int,sys.stdin.read().strip()))
if len(s) % 2 == 1: s.append(0)
X = []
i = 0
while i < len(s)-1:
    X.append([i//2, s[i], s[i+1]])
    i += 2
j = -1
while j > -len(X):
    i = 0
    while i < (len(X) + j):
        if X[i][2] >= X[j][1]:
            X.insert(i+1, [X[j][0], X[j][1], X[i][2] - X[j][1]])
            X[i][2] = 0
            X[j][2], X[j][1] = X[j][1]+X[j][2], 0
            break
        i += 1
    j -= 1
checksum = 0
n = 0
for id,rep,space in X:
    for _ in range(rep):
        checksum += n*id
        n += 1
    n += space
print(checksum)
