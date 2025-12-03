def leftmost_highest(nums, offset):
    res, idx = 0, 0
    for i, n in enumerate(nums):
        if n > res:
            res, idx = n, i
    return res, idx


res = 0

for line in open("puzzle.txt"):
    line = list(map(int, line.strip()))
    l, r = 0, len(line)-12
    cur = line[r:]
    sub_l = 0
    
    #print(f"=== \n {cur} - {line}")
    while sub_l < 12 and cur[sub_l] <= (candidate := leftmost_highest(line[l:r], l))[0]:
        #print(f"{cur}, {line[l:r]}")
        c, offset = candidate
        
        cur[sub_l] = c # new highest value found
        l += offset + 1 # where to start looking from
        sub_l += 1 # look for next element inside "window"
        r += 1 # sub_l but considering the entire array
    #print(cur)
    res += int(''.join(list(map(str, cur))))

print(res)
# too low -> 70575557661920