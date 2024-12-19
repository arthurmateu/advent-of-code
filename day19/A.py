# My first thought is just make a backtracking solution
towel_patterns, res = [], 0
check = True


def possible(towel):
    # check for patterns that are prefix to towel
    # remove prefix from towel
    # continue until you have no towel left
    return True if towel else False


for line in open("puzzle.txt"):
    if check:
        towel_patterns.extend(line.split(', '))
        towel_patterns[-1] = towel_patterns[-1][:-1] # remove '\n'
        check = False
    elif possible(line.split()):
        res += 1
