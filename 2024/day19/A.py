# My first thought is just make a backtracking solution
import functools

towel_patterns, res = [], -1 # to not count the first newline
check = True

@functools.cache
def possible(towel):
    if towel == '': 
        return True

    for pattern in towel_patterns:
        if towel.startswith(pattern) and possible(towel[len(pattern):]): 
            return True

    return False


for line in open("puzzle.txt"):
    if check:
        towel_patterns.extend(line.strip().split(', '))
        check = False
    elif possible(line.strip()):
            res += 1

print(res)
