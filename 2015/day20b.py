import numpy as np

lim = 10**6
n_presents = np.zeros(lim+1)

for elf in range(1, lim+1):
    for step in range(1, 50+1):
        i = elf*step
        if i <= lim:
            n_presents[i] += 11*elf

for i in range(len(n_presents)):
    if n_presents[i] >= 34000000:
        print(i)
        break