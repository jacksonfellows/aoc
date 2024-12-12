import sys

m = [list(line.strip()) for line in sys.stdin.readlines()]

VISITED = 0

drdc = ((-1,0),(1,0),(0,-1),(0,1))

def ff(r, c, letter, area, perimeter):
    if 0 <= r < len(m) and 0 <= c < len(m[0]):
        if m[r][c] == letter:
            m[r][c] = VISITED
            area += 1
            perimeter += sum(not (0 <= r + dr < len(m) and 0 <= c + dc < len(m[0])) or (m[r + dr][c + dc] != VISITED and m[r + dr][c + dc] != letter) for dr, dc in drdc)
            for dr, dc in drdc:
                area, perimeter = ff(r + dr, c + dc, letter, area, perimeter)
    return area, perimeter

cost = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if type(m[r][c]) == str:
            area, perimeter = ff(r, c, m[r][c], 0, 0)
            cost += area*perimeter
            VISITED += 1
print(cost)
