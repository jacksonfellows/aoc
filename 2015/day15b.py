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
calories = np.zeros(len(ingred))

for i,stats in enumerate(ingred.values()):
    c[i*4:(i+1)*4] = stats[:4]
    calories[i] = stats[-1]

def f(x):
    prod = -1
    for i in range(4):
        prod *= max(0,sum(x[j]*c[j*4+i] for j in range(len(ingred))))
    return prod

sol = scipy.optimize.minimize(fun=f, x0=100*np.ones(len(ingred))/len(ingred), bounds=[(0,100)]*len(ingred), constraints=[dict(type="eq", fun=lambda x: np.sum(x)-100), dict(type="eq", fun=lambda x: np.sum(x*calories)-500)], method="trust-constr")

down = np.floor(sol.x)
up = np.ceil(sol.x)

print(down, up)

max_f = 0
assert len(ingred)==4
for x0 in (down[0],up[0],down[0]-1,up[0]+1):
    for x1 in (down[1],up[1],down[1]-1,up[1]+1):
        for x2 in (down[2],up[2],down[2]-1,up[2]+1):
            for x3 in (down[3],up[3],down[3]-1,up[3]+1):
                xx = np.array((x0,x1,x2,x3))
                if np.sum(xx) == 100 and np.sum(xx*calories)==500:
                    max_f = max(max_f, int(-f(xx)))
                    print(xx, max_f)
print(max_f)