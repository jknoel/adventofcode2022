import numpy as np

grid = np.array([list(x.strip()) for x in open('input')], int)

part2 = np.ones_like(grid)

for _ in range(4): # 4 directions have symmetric code under rotation of grid
    for x,y in np.ndindex(grid.shape):
        lower = [t < grid[x,y] for t in grid[x,y+1:]]
        distanceToBiggerTree = next((i+1 for i,t in enumerate(lower) if ~t),len(lower))
        part2[x,y] *= distanceToBiggerTree
    grid, part2 = map(np.rot90, [grid, part2])

print(part2.max())
