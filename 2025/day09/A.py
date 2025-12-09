coords = []
for line in open("puzzle.txt"):
    x, y = map(int, line.strip().split(','))
    coords.append((x, y))
coords.sort()

res = 0
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        
        res = max(res, (x2-x1+1) * (y2-y1+1))

print(res)