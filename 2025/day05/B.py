ranges = list()

for line in open("puzzle.txt"):
    if '-' in line.strip():
        r = list(map(int, line.strip().split('-')))
        ranges.append(r)

ranges.sort()
c1, c2 = ranges[0]
res = 0

for r1, r2 in ranges:
    if r1 <= c2:
        c2 = max(c2, r2)
    else:
        res += c2 - c1 + 1
        c1, c2 = r1, r2

print(res + c2 - c1 + 1)