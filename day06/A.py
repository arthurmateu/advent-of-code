from collections import defaultdict
import sys
sys.setrecursionlimit(10000) # gave up lmao

grid = []
initial_r, initial_c, looking = 0, 0, True

with open("puzzle.txt") as file:
    for line in file:
        grid.append([ch for ch in line if ch != '\n'])
        if '^' in line: 
            initial_c = line.index('^')
            looking = False
        if looking: 
            initial_r += 1


ROWS, COLS = len(grid), len(grid[0])
visited = defaultdict(int) # I was getting some maximum recursion depth exceeded, so I assumed this would help
move = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_clockwise = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def helper(r, c, direction):
    if r==ROWS or c==COLS or r<0 or c<0 or visited[(r, c)] > 5: return
    visited[(r,c)] += 1
    if grid[r][c] == '#': # go back to previous move
        cancel_r, cancel_c = move[direction]
        return helper(r-cancel_r, c-cancel_c, turn_clockwise[direction])
    grid[r][c] = 'X'
    move_r, move_c = move[direction]
    return helper(r+move_r, c+move_c, direction)

helper(initial_r, initial_c, '^')

res = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'X': res += 1

print(res)
