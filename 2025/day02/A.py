# sequence of digits repeated twice

for line in open("puzzle.txt"):
    ranges = line.split(",")
    res = []
    for r in ranges:
        first, last = r.split("-")
        for d in range(int(first), int(last)+1):
            d = str(d)
            len_d = len(d)
            if d[:len_d//2] == d[len_d//2:]:
                res.append(int(d))

print(sum(res))