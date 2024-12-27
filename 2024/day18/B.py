import re
from collections import deque

ROWS, COLS = 71,71
grid = [['.']*COLS for _ in range(ROWS)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

# originally did dfs. it didn't work, WONDER WHY HUH
def attempt():
    queue = deque([(0,0,0)])
    visited = {(0,0)}
    while queue:
        r, c, s = queue.popleft()
        for rr, cc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if rr<0 or cc<0 or rr==ROWS or cc==COLS or grid[rr][cc]=='#' or (rr,cc) in visited: continue
            if rr==ROWS-1 and cc==COLS-1:
                return True
            visited.add((rr,cc))
            queue.append((rr,cc,s+1)) # why I'm getting an error here, nobody truly knows.
    return False

for line in open("puzzle.txt"):
    r, c = map(int, re.findall(r"\d+", line))
    grid[r][c] = '#'
    if not attempt():
        for row in grid:
            print(''.join(row))
        print(f"r={r},c={c}")
        exit(0)
