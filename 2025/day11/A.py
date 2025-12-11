from collections import defaultdict

adj = defaultdict(list)

for line in open("puzzle.txt"):
    vals = line.strip().split()
    src = vals[0][:-1]
    vals = vals[1:]

    for v in vals:
        adj[src].append(v)

q = ['you']
res = 0

while (x:=len(q)):
    for _ in range(x):
        node = q.pop(0)
        if node == 'out':
            res += 1
        
        for n in adj[node]:
            q.append(n)

print(res)