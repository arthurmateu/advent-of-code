# dijkstras ok. i can't implement this at all, i really struggle somehow
import heapq

grid = [list(line.strip()) for line in open("puzzle.txt")] # another cool one-liner i found on the YouTube channel mentioned previously
ROWS, COLS = len(grid), len(grid[0])
s, end = (0,0), (0,0)

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c]=='S': 
            s=(r,c)
            break

pq = [(0, *s, 0, 1)]
visited = {(*s, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    visited.add((r,c,dr,dc))
    if grid[r][c]=='E':
        print(cost)
        break
    for n_cost, nr, nc, ndr, ndc in [(cost+1, r+dr, c+dc, dr, dc), (cost+1000, r, c, dc, -dr), (cost+1000, r, c, -dc, dr)]:
        if grid[nr][nc] == '#' or (nr, nc, ndr, ndc) in visited: continue
        heapq.heappush(pq, (n_cost, nr, nc, ndr, ndc))
