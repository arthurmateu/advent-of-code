def backtrack(i, j, cur, lights, taken):
    if i == j:
        if cur == lights:
            steps.append(taken)
        return 
    
    # option 1: take current button presses
    tmp = cur.copy()
    for k in options[i][1:-1].split(','):
        k = int(k)
        cur[k] = (cur[k] + 1) % 2
    #print(f"CURRENT CUR -> {cur}")
    backtrack(i+1, j, cur, lights, taken+1)
    
    # option 2: dont
    #print(f"CURRENT CUR (STEP NOT TAKEN) -> {tmp}")
    backtrack(i+1, j, tmp, lights, taken)


res = 0

for line in open("puzzle.txt"):
    line = line.strip().split()

    lights = []
    for i in range(len(line[0])):
        if line[0][i] in '[]': continue
        if line[0][i] == '.': lights.append(0)
        else: lights.append(1)
    
    options = line[1:-1]
    j = len(options)
    cur = [0] * (len(lights))
    options = line[1:-1]

    steps = []

    #print(f"CURRENTLY CHECKING FOR {j} | {cur} | {lights} - OPTIONS ARE {options}")

    backtrack(0, j, cur, lights, 0)
    #print("===")
    steps.sort()
    res += steps[0]

print(res)