process, last_file_id = [], 0
with open("test.txt") as file:
    for line in file:
        file_id = 0
        checking_files = True
        for i in range(len(line)-1):
            if checking_files:
                process.extend([str(file_id)]*int(line[i]))
                file_id += 1
                checking_files = False
            else:
                process.extend(['.']*int(line[i]))
                checking_files = True
        last_file_id = file_id

print(process)

N = len(process)
def check_space(amount_required):
    window, i = 0, 0
    while i < N:
        while process[i] == '.':
            if window-i == amount_required:
                return window
            i += 1
        i += 1
        window = i
    return -1

l, r = N-1, N-1

while last_file_id > 0:
    amount_required = 0
    while process[r] == process[l]:
        l -= 1
    # basically just calculate window size to be switched, switch (if check_space > 0) and then go to the next one.

    last_file_id -= 1

res = 0
for i in range(len(process)):
    if process[i][0] != '.':
        res += int(process[i][0]) * i

print(res)
