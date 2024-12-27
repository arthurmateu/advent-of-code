# heavily inspired by a solution i saw on the python server (username ._.bulka)
def check_safe(line):
    return (all(line[i] < line[i + 1] and line[i + 1] - line[i] <= 3 for i in range(len(line) - 1)) or all(line[i] > line[i + 1] and line[i] - line[i + 1] <= 3 for i in range(len(line) - 1)))

res = 0

with open("puzzle.txt") as file:
    for line in file:
        nums = [int(x) for x in line.split()]
        # could've merged both into a single, very long if statement. imagine why i didnt do that!
        if check_safe(nums): res += 1
        else:
            nums = [nums[:i]+nums[i+1:] for i in range(len(nums))]
            if any(check_safe(n) for n in nums): res += 1

print(res)
