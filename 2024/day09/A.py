process = []
with open("puzzle.txt") as file:
    for line in file:
        cur = 0
        checking_files = True
        for i in range(len(line)-1):
            if checking_files:
                process.extend([str(cur)] * int(line[i]))
                cur += 1
                checking_files = False
            else:
                process.extend(['.'] * int(line[i]))
                checking_files = True

l, r = 0, len(process)-1
steps = process.count('.')

while process[-steps:].count('.') != steps:
    while process[l].isnumeric():
        l += 1
    while not process[r].isnumeric(): 
        r -= 1
    else:
        process[l], process[r] = process[r], process[l]

res = 0
for i in range(len(process)-steps):
    res += int(process[i])*i

print(res)
