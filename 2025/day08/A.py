from collections import defaultdict
import math

coords = []
for line in open("puzzle.txt"):
    coords.append(tuple(map(int, line.strip().split(','))))
N = len(coords)

dist = []
for i in range(N):
    for j in range(i+1, N):
        a = coords[i]
        b = coords[j]
        euclidean = math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2 )
        dist.append([euclidean, i, j])
dist.sort()

parent = {v: v for v in range(N)} # make_set

def find_set(v):
    if v == parent[v]:
        return v
    return find_set(parent[v])

def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        parent[b] = a

for i in range(1000):
    _, a, b = dist[i]
    union_sets(a, b)

cnt = defaultdict(int)
for i in range(N):
    cnt[find_set(i)] += 1
res = sorted(cnt.values())

print(res[-1]*res[-2]*res[-3])