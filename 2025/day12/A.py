pieces = {0:6, 1:7, 2:5, 3:7, 4:7, 5:7} # hardcoded from helper.txt, idc
res = 0

for line in open("puzzle.txt"):
    line = line.strip().split()
    x, y = map(int, line[0][:-1].split("x"))
    total_area = x*y

    qnt = list(map(int, line[1:]))

    for v, q in zip(pieces.values(), qnt):
        total_area -= v*q

    res += total_area >= 0

print(res)