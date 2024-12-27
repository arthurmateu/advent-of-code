import re

registers, program = [], []
for line in open("puzzle.txt"):
    if len(registers)==3:
        program = list(map(int, re.findall(r"\d+", line)))
    else:
        registers.append(int(*re.findall(r"\d+", line)))

for i in program:
    if i == 0: pass #division
    elif i == 1: pass #division xor
    elif i == 2: pass #combo
    elif i == 3: pass #nothing
    elif i == 4: pass # bitwise xor
    elif i == 5: pass #combo
    elif i == 6: pass #store
    else: pass #7
