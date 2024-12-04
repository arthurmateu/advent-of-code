# quite possibly the most abhorrent code ever conceived. PART TWO!!!!!
def has_xmas(r, c):
    total = 0
    if grid[r+1][c+1] == "A":
        # MSAMS
        if (grid[r][c] == grid[r+2][c] == "M") and (grid[r][c+2] == grid[r+2][c+2] == "S"): total += 1
        # SMASM
        if (grid[r][c] == grid[r+2][c] == "S") and (grid[r][c+2] == grid[r+2][c+2] == "M"): total += 1
        # MMASS
        if (grid[r][c] == grid[r][c+2] == "M") and (grid[r+2][c] == grid[r+2][c+2] == "S"): total += 1
        # SSAMM
        if (grid[r][c] == grid[r][c+2] == "S") and (grid[r+2][c] == grid[r+2][c+2] == "M"): total += 1
    return total

res, grid = 0, []

with open("puzzle.txt") as file:
    for line in file: grid.append(line)

ROWS, COLS = len(grid), len(grid[0])

for r in range(ROWS-2):
    for c in range(COLS-2):
        res += has_xmas(r, c)


print(res)
