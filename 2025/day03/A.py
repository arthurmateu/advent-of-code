res = 0

for line in open("puzzle.txt"):
    l, cur = 0, 0
    line = list(map(int, line.strip()))

    for r in range(1, len(line)):
        cur = max(cur, line[l]*10 + line[r])
        if line[r] > line[l]:
            l = r

    res += cur

print(res)