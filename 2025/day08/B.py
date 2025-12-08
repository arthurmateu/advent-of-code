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
    parent[b] = a

cnt = 0
for _, i, j in dist:
    if find_set(i) != find_set(j):
        cnt += 1
        if cnt == N-1:
            print(coords[i][0] * coords[j][0])# res
            break
        union_sets(i, j)