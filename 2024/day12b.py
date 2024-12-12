import sys

# import matplotlib.pyplot as plt

m = [list(line.strip()) for line in sys.stdin.readlines()]

VISITED = 0

drdc = ((-1,0),(1,0),(0,-1),(0,1))

def ff(r, c, letter, area, edges):
    if 0 <= r < len(m) and 0 <= c < len(m[0]):
        if m[r][c] == letter:
            m[r][c] = VISITED
            area += 1
            E = (((r, c), (r, c+1)),
                 ((r+1, c), (r+1, c+1)),
                 ((r, c), (r+1, c)),
                 ((r, c+1), (r+1, c+1)))
            edges += tuple(edge for (dr, dc), edge in zip(drdc, E) if not (0 <= r + dr < len(m) and 0 <= c + dc < len(m[0])) or (m[r + dr][c + dc] != VISITED and m[r + dr][c + dc] != letter))
            for dr, dc in drdc:
                area, edges = ff(r + dr, c + dc, letter, area, edges)
    return area, edges

def dirr(edge):
    (r1,c1),(r2,c2) = edge
    return r1 == r2, c1 == c2

def combine(edges):
    edges = list(edges)
    dirty = True
    while dirty:
        dirty = False
        i = 0
        while i < len(edges):
            j = i + 1
            while j < len(edges):
                e1 = edges[i]
                a,b = e1
                e2 = edges[j]
                c,d = e2
                for x,y,w,z in ((a,c,b,d),(a,d,b,c),(b,c,a,d),(b,d,a,c)):
                    if x == y and dirr(e1) == dirr(e2):
                        if not any(k != i and k != j and (x == m or x == n) for k,(m,n) in enumerate(edges)):
                            edges[i] = (w, z)
                            del edges[j]
                            dirty = True
                            break
                j += 1
            i += 1
    return tuple(edges)

cost = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if type(m[r][c]) == str:
            area, edges = ff(r, c, m[r][c], 0, ())
            edges = combine(edges)
            # print(area, len(edges))
            # plt.gca().set_aspect("equal")
            # plt.ylim(len(m)+1, -1)
            # plt.xlim(-1, len(m[0])+1)
            # for (r1,c1),(r2,c2) in edges:
            #     plt.plot((c1,c2), (r1,r2))
            # plt.show()
            cost += area * len(edges)
            VISITED += 1
print(cost)
