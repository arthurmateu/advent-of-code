# My first thought is just make a backtracking solution
import functools

towel_patterns, res = [], -1 # to not count the first newline
check = True

@functools.cache
def possible(towel):
    if towel == '': 
        return 1

    possibilities = 0
    for pattern in towel_patterns:
        if towel.startswith(pattern): 
            possibilities += possible(towel[len(pattern):])

    return possibilities


for line in open("puzzle.txt"):
    if check:
        towel_patterns.extend(line.strip().split(', '))
        check = False
    else:
        res += possible(line.strip())

print(res)
