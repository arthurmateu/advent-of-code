from collections import defaultdict
from functools import cache

adj = defaultdict(list)

for line in open("puzzle.txt"):
    vals = line.strip().split()
    src = vals[0][:-1]
    vals = vals[1:]

    for v in vals:
        adj[src].append(v)

# bfs was being annoying
@cache
def dfs(cur='svr', dac=False, fft=False):
    if cur == 'dac': dac = True
    if cur == 'fft': fft = True
    if cur == 'out': return dac and fft
    return sum(dfs(n, dac, fft) for n in adj[cur])

print(dfs())