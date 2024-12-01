from collections import Counter, defaultdict

l1, l2, res = [], [], 0
with open("puzzle_01.txt") as file:
    for line in file:
        n1, n2 = (int(x) for x in line.split())
        l1.append(n1)
        l2.append(n2)

cnt = defaultdict(int)
for k, v in Counter(l2).items():
    cnt[k] = k*v


for n in l1:
    res += cnt[n]

print(res)
