import re


# NEW INFO! - found on HyperNeutrino's YouTube channel
# Apparently there's a better way to read the file:
# for block in open("").read().split("\n\n"):
#     ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block)

cases = []
with open("puzzle.txt") as file:
    case = []
    for line in file:
        case.append(line.strip())
        if len(case) == 4:
            cases.append(case)
            case = []

# I was trying to get straight into the part 2 solution/aka "most efficient". 
# I didn't really think you could brute force it with two for loops (if there's two loops involved, I just automatically assume it's wrong and just keep thinking through the problem).
# Sadly, since I can't recall my entire highschool math classes, I had to look up some hints. I assumed you had just an equation with two variables, but when I tried to solve it that way, I didn't have any clue on how to translate it into code
def find_least(button_a, button_b, prize):
    px, py = (p for p in prize)
    ax, ay = (a for a in button_a)
    bx, by = (b for b in button_b)

    ca = (px*by - py*bx) / (ax*by - ay*bx)
    cb = (px - ax*ca) / bx

    return int(3*ca+cb) if ca%1==0 and cb%1==0 and ca<=100 and cb<=100 else 0


numbers = r"(\d+), Y[\+|=](\d+)"
res = 0
for case in cases:
    button_a = [int(x) for match in re.findall(numbers, case[0]) for x in match]
    button_b = [int(x) for match in re.findall(numbers, case[1]) for x in match]
    prize = [int(x) for match in re.findall(numbers, case[2]) for x in match]

    res += find_least(button_a, button_b, prize)

print(res)
