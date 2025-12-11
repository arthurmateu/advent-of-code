from collections import defaultdict
import z3

res = 0

for line in open("puzzle.txt"):
    line = line.strip().split()

    joltages = list(map(int, line[-1][1:-1].split(',')))
    options = list(tuple(map(int, o[1:-1].split(","))) for o in line[1:-1])

    N = len(options)

    solver = z3.Optimize()
    vars = list(z3.Int(f"x{i}") for i in range(N))
    used = defaultdict(int)
        
    for i in range(N):
        solver.add(vars[i] >= 0)
        for pos in options[i]:
            used[pos] += vars[i]

    for idx, num in enumerate(joltages):
        solver.add(used[idx] == num)

    solver.minimize(sum(vars))
    if solver.check() == z3.sat: # otherwise it breaks
        model = solver.model()
        res += sum(model[v].as_long() for v in vars)

print(res)