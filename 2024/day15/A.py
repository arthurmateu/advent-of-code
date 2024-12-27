grid, moves = [], []
check = True

for line in open("puzzle.txt").read().split("\n\n"):
    if check:
        for l in line.split('\n'):
            cur = []
            for ch in l:
                cur.append(ch)
            grid.append(cur)
        check = False
    else:
        moves.extend(c for c in line if c != '\n')

equiv = {'^': (-1, 0),
         '>': (0,1),
         '<': (0,-1),
         'v': (1, 0)}
ROWS, COLS = len(grid), len(grid[0])
fx, fy = 0, 0

# LOCATE FISH/ROBOT
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '@': 
            fx, fy = r, c
            break



for m in moves:
    #print(f"CURRENT MOVEMENT = {m}")
    #for r in grid:
    #    print(''.join(r))
    #print()

    mx, my = equiv[m]

    if grid[fx+mx][fy+my] == '.':
        grid[fx+mx][fy+my] = '@'
        grid[fx][fy] = '.'
        fx += mx
        fy += my


    elif grid[fx+mx][fy+my] == 'O':

        ex, ey = fx+mx, fy+my
        e = grid[ex][ey]
        found = False

        while e != '#':
            ex += mx
            ey += my
            e = grid[ex][ey]
            if e=='.':
                found = True
                break

        if found:
            grid[ex][ey] = 'O'
            grid[fx+mx][fy+my] = '@'
            grid[fx][fy] = '.'
            fx += mx
            fy += my


    else: # it's a wall
        continue



res = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'O': 
            res += 100*r+c
print(res)
