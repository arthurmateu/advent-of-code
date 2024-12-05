import re
from graphlib import TopologicalSorter
from collections import defaultdict

rules, produced = r"(\d+)\|(\d+)", r","
appears_before, appears_after = defaultdict(list), defaultdict(list)
res, incorrect = 0, []

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
                    incorrect.append(values)
                    break
                cant_appear.update(appears_after[el])

for li in incorrect:
    graph = {}
    for el in li:
        graph[el] = [i for i in appears_before[el] if i in li]
    li = list(TopologicalSorter(graph).static_order()) # had to look this concept up
    res += int(li[len(li)//2])

print(res)
