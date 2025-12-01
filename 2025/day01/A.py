# Rx -> +x
# Lx -> -x
# Cycles 0 99. Begins at 50
# Count how many times it reaches 0

res = 0
dial = 50

for line in open("puzzle.txt"):
    line = line.strip()
    if line[0] == 'R':
        dial += int(line[1:])
    else:
        dial -= int(line[1:])

    dial %= 100

    if dial == 0:
        res += 1
    #print(f"line={line}, dial={dial}, res={res}")

print(res)