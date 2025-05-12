import sys
from itertools import product

grid = [[False,*[c=="#" for c in line.strip()],False] for line in sys.stdin.readlines()]
grid = [[False]*len(grid[0]),*grid,[False]*len(grid[0])]

for _ in range(100):
    next_grid = [[False]*len(grid[0]) for _ in range(len(grid))]
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            n_neighbors = sum(grid[r+dr][c+dc] for dr,dc in product([-1,0,1],[-1,0,1]) if not (dr==0 and dc==0))
            if grid[r][c]:
                next_grid[r][c] = n_neighbors == 2 or n_neighbors == 3
            else:
                next_grid[r][c] = n_neighbors == 3
    grid = next_grid

#print("\n".join(["".join(["#" if x else "." for x in row]) for row in grid]))
print(sum(sum(row) for row in grid))
