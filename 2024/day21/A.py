from functools import cache

res, ignore = 0, set()

adjacent = {
    '0': ['2', 'A'],
    '1': ['2', '4'],
    '2': ['0', '1', '3', '5'],
    '3': ['2', '6', 'A'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9'],
    '9': ['6', '8'],
    'A': ['0', '3'],
}

# idk, adjacency list was clearly ignoring that 6 can go to 9. also there are a ton of other steps I've forgotten to take.
@cache
def shortest_sequence(remaining, start='A', moves=0):
    global ignore

    if not remaining:
        return moves

    if start == remaining[0]:
        ignore = set()
        return shortest_sequence(remaining[1:], start, moves+1)

    ignore.add(start)

    return min(shortest_sequence(remaining, a, moves+1) for a in adjacent[start] if a not in ignore)



for line in open("test.txt"):
    res += shortest_sequence(line.strip()) * int(line.strip()[:-1])

print(res)
