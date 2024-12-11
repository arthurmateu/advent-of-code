# 0s become 1s
# even digits become 2 stones [left digits going to left one, right ones to right]
# otherwise, stone number * 2024
# order is preserved

stones = []
with open("puzzle.txt") as file:
    for line in file:
        stones.extend([int(x) for x in line.split()])

for i in range(25):
    s, original_length = 0, len(stones)
    while s < original_length:
        string_stone = str(stones[s])
        if stones[s] == 0: 
            stones[s] = 1
        elif len(string_stone) % 2 == 0:
            mid_point = len(string_stone)//2
            l_stone, r_stone = int(string_stone[:mid_point]), int(string_stone[mid_point:])
            stones = stones[:s] + [l_stone, r_stone] + stones[s+1:]
            s += 1
            original_length += 1
        else:
            stones[s] *= 2024
        s += 1

print(len(stones))
