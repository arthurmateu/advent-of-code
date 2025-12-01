# Rx -> +x
# Lx -> -x
# Cycles 0 99. Begins at 50
# Count how many times it "ticks" 0

res = 0
dial = 50

for line in open("puzzle.txt"):
    line = line.strip()
    rot = int(line[1:])
    prev = dial

    if line[0] == 'R': dial += rot
    else: dial -= rot


    if dial <= 0 and prev != 0: res += 1 # ts so ahh
    res += abs(dial)//100

    #print(f"line={line}, dial={dial}, res={res}")
    dial %= 100

print(res)