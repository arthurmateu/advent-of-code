import re

res = 0
pattern = r"mul\((\d+),(\d+)\)" # thanks pythex for existing

with open("puzzle.txt") as file:
    for line in file:
        for match in re.findall(pattern, line):
            res += int(match[0])*int(match[1])

print(res)
