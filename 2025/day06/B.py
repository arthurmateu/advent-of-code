values = []

for line in open("puzzle.txt"):
    values.append(list(l for l in line if l != '\n'))

symbols = ''.join(values[-1]).split()
s = 0

values = values[:-1]
res = 0

ROWS, COLS = len(values), len(values[0])

cur = []
for c in range(COLS+1): # include last val

    if c == COLS or all( values[r][c] == ' ' for r in range(ROWS) ): # entire column is actually a space between problems
        
        if symbols[s] == '+':
            res += sum(map(int, cur))
        else:
            mult = 1
            for val in map(int, cur): mult *= val
            res += mult

        s += 1
        cur = []

    else:
        d = ''
        for r in range(ROWS):
            d += values[r][c] if values[r][c] != ' ' else ''
        cur.append(d)

print(res)