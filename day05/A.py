import re
from collections import defaultdict

rules, produced = r"(\d+)\|(\d+)", r","
appears_before, appears_after = defaultdict(list), defaultdict(list)
res = 0

with open("puzzle.txt") as file:
    for line in file:
        if re.search(rules, line):
            f=re.findall(rules, line)
            pre, pos = f[0][0], f[0][1]
            appears_before[pos].append(pre) # didn't really use it but I'm saving it
            appears_after[pre].append(pos)

        elif re.search(produced, line):
            values, cant_appear, valid = line.split(","), set(), True
            values[-1] = values[-1][:-1]
            for el in reversed(values):
                if el in cant_appear:
                    valid = False
                    break
                cant_appear.update(appears_after[el])
            if valid: 
                middle = int(values[len(values)//2])
                res += middle

print(res)
