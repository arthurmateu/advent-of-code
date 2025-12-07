from functools import cache

start_col = 0
splitters = set()
total_rows = 0

for line in open("puzzle.txt"):
    for c, s in enumerate(line):
        if s == 'S':
            start_col = c
        elif s == '^':
            splitters.add((total_rows, c))
    total_rows += 1

@cache
def dfs(r=0, c=start_col):
    if r == total_rows: 
        return 1
    
    if (r, c) in splitters:
        return dfs(r+1, c+1) + dfs(r+1, c-1)

    return dfs(r+1, c)

print(dfs())