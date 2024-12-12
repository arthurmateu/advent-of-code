grid = []
with open("puzzle.txt") as file:
    for line in file:
        grid.append([int(ch) for ch in line.strip()])

ROWS, COLS = len(grid), len(grid[0])
res = 0
def dfs(r, c, prev, visited):
    if r == ROWS or c == COLS or r < 0 or c < 0 or prev+1 != grid[r][c] or (r,c) in visited: return 0
    visited.add((r,c))
    if grid[r][c] == 9: return 1
    ns, nei = prev+1, [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return sum(dfs(r+rr, c+cc, ns, visited) for rr, cc in nei)


for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c]==0:
            res += dfs(r, c, -1, set()) # tried putting set() inside the dfs itself, but it didn't work at all.

print(res)