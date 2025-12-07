mat = []

for line in open("puzzle.txt"):
    mat.append(list(line.strip()))

ROWS, COLS = len(mat), len(mat[0])
start_row, start_col = 0, mat[0].index('S')+1
heap = [(start_row, start_col-1)]
visited = set((start_row, start_col))
res = 0

while heap:
    for _ in range(len(heap)):
        r, c = heap.pop(0)
        if 0 <= r < ROWS and 0 <= c < COLS:
            if mat[r][c] == '|': continue
            
            if mat[r][c] == '^':
                res += 1
                heap.append((r+1, c+1))
                heap.append((r+1, c-1))
            else:
                heap.append((r+1, c))
            mat[r][c] = '|'

#for r in mat:
#    print(''.join(r))

print(res)