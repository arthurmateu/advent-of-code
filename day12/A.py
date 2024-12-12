grid = []
with open("puzzle.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

ROWS, COLS = len(grid), len(grid[0])
neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(r, c, region):
    if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c] != region: return (0,1)
    if (r,c) in visited: return (0,0)
    visited.add((r,c))
    area, perimeter = 1, 0
    for nei_area, nei_perimeter in (dfs(r+nr, c+nc, region) for nr,nc in neighbours):
        area += nei_area
        perimeter += nei_perimeter
    return area, perimeter

res, visited = 0, set()
for r in range(ROWS):
    for c in range(COLS):
        area, perimeter = dfs(r, c, grid[r][c])
        res += area * perimeter

print(res)
