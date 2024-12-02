res = 0

with open("puzzle.txt") as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        if (sorted(nums) == nums or sorted(nums, reverse=True) == nums) and all(1 <= abs(nums[i]-nums[i-1]) <=3 for i in range(1,len(nums))):
            res += 1

print(res)
