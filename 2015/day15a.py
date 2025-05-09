import sys
import re
import scipy.optimize
import numpy as np
import itertools

r = re.compile("^(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)$")

ingred = {}
for line in sys.stdin.readlines():
    m = r.match(line)
    ingred[m[1]] = np.array([int(m[i]) for i in range(2,7)])

c = np.zeros(4*len(ingred))

for i,stats in enumerate(ingred.values()):
    c[i*4:(i+1)*4] = stats[:4]

def f(x):
    prod = -1
    for i in range(4):
        prod *= max(0,sum(x[j]*c[j*4+i] for j in range(len(ingred))))
    return prod

sol = scipy.optimize.minimize(fun=f, x0=100*np.ones(len(ingred))/len(ingred), bounds=[(0,100)]*len(ingred), constraints=[dict(type="eq", fun=lambda x: np.sum(x)-100)], method="trust-constr")

down = np.floor(sol.x)
up = np.ceil(sol.x)

max_f = 0
assert len(ingred)==4
for x0 in (down[0],up[0]):
    for x1 in (down[1],up[1]):
        for x2 in (down[2],up[2]):
            for x3 in (down[3],up[3]):
                xx = np.array((x0,x1,x2,x3))
                if np.sum(xx) == 100:
                    max_f = max(max_f, int(-f(xx)))
print(max_f)