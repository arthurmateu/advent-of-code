l1, l2, res = [], [], []
with open("puzzle_01.txt") as file:
    for line in file:
        n1, n2 = (int(x) for x in line.split())
        l1.append(n1)
        l2.append(n2)

l1.sort()
l2.sort()

for i in range(len(l1)):
    res.append(abs(l1[i]-l2[i]))

print(sum(res))
