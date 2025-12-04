mat = []
for line in open("puzzle.txt"):
    mat.append(list(line.strip()))

ROWS, COLS = len(mat), len(mat[0])
res = 0

for _ in range(3000): # lazy
    for r in range(ROWS):
        for c in range(COLS):
            if mat[r][c] == '@':
                cur = 0
                for (x, y) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]:
                    if 0 <= x < ROWS and 0 <= y < COLS and mat[x][y] == '@':
                        cur += 1
                if cur < 4:
                    mat[r][c] = '.'
                    res += 1
                    
print(res)