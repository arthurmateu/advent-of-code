import re
from collections import deque

ROWS, COLS, LIMIT = 71,71,1024
grid = [['.']*COLS for _ in range(ROWS)]
corrupted = 0

for line in open("puzzle.txt"):
    if corrupted == LIMIT: break
    r, c = map(int, re.findall(r"\d+", line))
    grid[r][c] = '#'
    corrupted += 1

directions = [(1,0), (-1,0), (0,1), (0,-1)]
queue, visited = deque([(0,0,0)]), {(0,0)}

# originally did dfs. it didn't work, WONDER WHY HUH
while queue:
    r, c, s = queue.popleft()
    for rr, cc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if rr<0 or cc<0 or rr==ROWS or cc==COLS or grid[rr][cc]=='#' or (rr,cc) in visited: continue
        if rr==ROWS-1 and cc==COLS-1:
            print(s+1)
            exit(0)
        visited.add((rr,cc))
        queue.append((rr,cc,s+1)) # why I'm getting an error here, nobody truly knows.
