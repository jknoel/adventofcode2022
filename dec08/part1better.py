import numpy as np

grid = np.array([list(x.strip()) for x in open('testInput')], int)

part1 = np.zeros_like(grid)

for _ in range(4):
    for x,y in np.ndindex(grid.shape):
        lower = [t < grid[x,y] for t in grid[x,y+1:]]
        part1[x,y] |= np.all(lower)
    grid, part1 = map(np.rot90, [grid, part1])

print(part1.sum())