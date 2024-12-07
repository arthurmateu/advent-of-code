def isValid(expected, values):
    a, b = values[0], values[1]
    if len(values) == 2:
        return expected == a+b or expected == a*b or expected == int(str(a)+str(b))

    values = values[2:]
    sum_path = [a+b] + values
    mult_path = [a*b] + values
    conc_path = [int(str(a)+str(b))] + values

    return isValid(expected, sum_path) or isValid(expected, mult_path) or isValid(expected, conc_path)


res = 0
with open("puzzle.txt") as file:
    for line in file:
        expected = ""
        for i in range(len(line)):
            if line[i] == ':': 
                line = line[i+2:]
                break
            expected += line[i]
        expected = int(expected)
        values = [int(x) for x in line.split()]
        if isValid(expected, values):
            res += expected

print(res)
