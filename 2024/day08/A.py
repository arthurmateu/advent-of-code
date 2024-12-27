from collections import defaultdict
# Basically, find every similar characters.
# Calculate its difference (for example x=1, y=2) and see if it's a free space of if there's another character there.

grid = []

with open("puzzle.txt") as file:
    for line in file:
        grid.append([ch for ch in line if ch != '\n'])

ROWS, COLS = len(grid), len(grid[0])
ch_locations= defaultdict(list)
for r in range(ROWS):
    for c in range(COLS):
        ch = grid[r][c]
        if ch == '.': continue
        else: ch_locations[ch].append([r, c])

antennas = ch_locations.keys()

for ch, coord_list in ch_locations.items():
    for i in range(len(coord_list)):
        for j in range(i+1, len(coord_list)):
            r1, r2 = coord_list[i][0], coord_list[j][0]
            c1, c2 = coord_list[i][1], coord_list[j][1]

            rd = r1 - r2
            cd = c1 - c2

            if 0 <= (rf:=r1+rd) < ROWS and 0 <= (cf:=c1+cd) < COLS:
                if grid[rf][cf] == '.' or grid[rf][cf] in antennas: 
                    grid[rf][cf] = '#'
            if 0 <= (rs:=r2-rd) < ROWS and 0 <= (cs:=c2-cd) < COLS:
                if grid[rs][cs] == '.' or grid[rs][cs] in antennas:  
                    grid[rs][cs] = '#'

print(sum(row.count('#') for row in grid))
