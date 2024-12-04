# quite possibly the most abhorrent code ever conceived
def has_xmas(r, c):
    total = 0
    # horizontal
    if c+3 < COLS:
        if (grid[r][c]=='X' and grid[r][c+1]=='M' and grid[r][c+2]=='A' and grid[r][c+3]=='S') or (grid[r][c]=='S' and grid[r][c+1]=='A' and grid[r][c+2]=='M' and grid[r][c+3]=='X'): total += 1
    # vertical
    if r+3 < ROWS:
        if (grid[r][c]=='X' and grid[r+1][c]=='M' and grid[r+2][c]=='A' and grid[r+3][c]=='S') or (grid[r][c]=='S' and grid[r+1][c]=='A' and grid[r+2][c]=='M' and grid[r+3][c]=='X'): total += 1
    # diagonal
    if r+3 < ROWS and c+3 < COLS:
        if (grid[r][c]=='X' and grid[r+1][c+1]=='M' and grid[r+2][c+2]=='A' and grid[r+3][c+3]=='S') or (grid[r][c]=='S' and grid[r+1][c+1]=='A' and grid[r+2][c+2]=='M' and grid[r+3][c+3]=='X'): total += 1
    # reverse diagonal
    if r+3 < ROWS and c-3 >= 0:
        if (grid[r][c]=='X' and grid[r+1][c-1]=='M' and grid[r+2][c-2]=='A' and grid[r+3][c-3]=='S') or (grid[r][c]=='S' and grid[r+1][c-1]=='A' and grid[r+2][c-2]=='M' and grid[r+3][c-3]=='X'): total += 1
    return total

res, grid = 0, []

with open("puzzle.txt") as file:
    for line in file: grid.append(line)

ROWS, COLS = len(grid), len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        res += has_xmas(r, c)


print(res)
