res = 0
ranges = list()

for line in open("puzzle.txt"):
    if line.strip() == '': 
        continue

    elif '-' not in line.strip():
        for s, e in ranges:
            if s <= int(line.strip()) <= e:
                res += 1
                break
    
    else:
        r = list(map(int, line.strip().split('-')))
        ranges.append(r)

print(res)