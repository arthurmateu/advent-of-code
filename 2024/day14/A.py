from functools import reduce
import re
WIDE, TALL = 101, 103
HW, HT = (WIDE-1)//2, (TALL-1)//2

quadrants = [0, 0, 0, 0]
with open("puzzle.txt") as file:
    for robot in file:
        px, py, vx, vy = map(int, re.findall(r"-?\d+", robot))
        # calculate all final position after 100 seconds. use mod to put back into grid
        x = (px + 100*vx) % WIDE
        y = (py + 100*vy) % TALL

        if x==HW or y==HT: continue # middle

        # yes, theres probably a formula that does these if statements in one line.
        if y<HT:
            if x<HW: quadrants[0] += 1
            else: quadrants[1] += 1
        else:
            if x<HW: quadrants[2] += 1
            else: quadrants[3] += 1

print(reduce(lambda x,y:x*y, quadrants))
