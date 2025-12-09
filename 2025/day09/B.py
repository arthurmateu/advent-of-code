from shapely.geometry import Polygon

red = []
for line in open("puzzle.txt"):
    x, y = map(int, line.strip().split(','))
    red.append((x, y))

total = Polygon(red)

res = 0
for i in range(len(red)):
    for j in range(i+1, len(red)):
        a, b = red[i], red[j]
        if total.covers(Polygon([a, (a[0], b[1]), b, (b[0], a[1])])):
            res = max(res, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))

print(res)

previous_attempt = """
import sys
sys.setrecursionlimit(100000)

ROWS, COLS = 0, 0
red = []

def get_vals(a, b):
    x1, x2 = a[0], b[0]
    y1, y2 = a[1], b[1]

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    return x1, x2, y1, y2

for line in open("puzzle.txt"):
    x, y = map(int, line.strip().split(','))
    red.append((x, y))
    ROWS, COLS = max(ROWS, x), max(COLS, y)

red.sort()
N = len(red)


# Make grid
mat = [['.'] * (COLS) for _ in range((ROWS))]
def debug():
    for r in mat:
        print(' '.join(r))

for x, y in red:
    mat[x-1][y-1] = 'R'

def extend(a, b):
    x1, x2, y1, y2 = get_vals(a, b)

    if x1 == x2:
        for c in range(y1, y2-1):
            mat[x1-1][c] = 'G'
    elif y1 == y2:
        for r in range(x1, x2-1):
            mat[r][y1-1] = 'G'

for i in range(N):
    for j in range(i+1, N):
        extend(red[i], red[j])

# bucket fill
def bucket_fill(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS and mat[r][c] == '.':
        mat[r][c] = 'G'
        bucket_fill(r+1, c)
        bucket_fill(r-1, c)
        bucket_fill(r, c+1)
        bucket_fill(r, c-1)

for x, y in red:
    x -= 1
    y -= 1
    if x+1 <= ROWS and y+1 < COLS and mat[x+1][y] in 'GR' and mat[x][y+1] in 'GR':
        bucket_fill(x+1, y+1)
        break

# check between coords
def check_valid(a, b):
    x1, x2, y1, y2 = get_vals(a, b)
    for r in range(x1, x2):
        for c in range(y1, y2):
            if mat[r][c] not in 'GR': 
                return False
    return True

res = 0
for i in range(N):
    for j in range(i+1, N):
        a, b = red[i], red[j]
        if check_valid(a, b):
            x1, x2, y1, y2 = get_vals(a, b)
            res = max(res, (x2-x1+1) * (y2-y1+1))

print(res)
"""