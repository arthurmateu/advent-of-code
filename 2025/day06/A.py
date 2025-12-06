vals = []
for line in open("puzzle.txt"):
    vals.append(line.strip().split())

things = vals[-1]
vals = vals[:-1]
res = 0

ROWS, COLS = len(vals), len(vals[0])

for c in range(COLS):
    col = []
    for r in range(ROWS):
        col.append(vals[r][c])
    print(col)

    if things[c] == '+':
        res += sum(map(int, col))
    else:
        cur = 1
        for val in map(int, col): cur *= val
        res += cur


print(res)