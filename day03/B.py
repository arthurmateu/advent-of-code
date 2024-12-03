import re

res = 0
#mul_pattern = r"mul\((\d+),(\d+)\)" - thanks pythex for existing
#do_pattern = r"do\(\)"
#dont_pattern = r"don\'t\(\)"

all_patterns = r"(mul\((\d+),(\d+)\)|do(n\'t)?\(\))"
status = True # "At the beginning of the program..." this line messed me up.

with open("puzzle.txt") as file:
    for line in file:
        findings = re.findall(all_patterns, line)
        for f in findings:
            if f[0] == "do()":
                status = True
            elif f[0] == "don't()":
                status = False
            else:
                if status: res += int(f[1]) * int(f[2])


print(res)
