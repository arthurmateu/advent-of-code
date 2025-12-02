# sequence of digits repeated

for line in open("puzzle.txt"):
    ranges = line.split(",")
    res = []
    for r in ranges:
        first, last = r.split("-")

        for d in range(int(first), int(last)+1):
            stop = False
            d = str(d)
            len_d = len(d)

            # Split into parts with length {i}
            for i in range(1, len_d//2+1):
                if len_d % i != 0: continue # skip

                s = set(d[j:j+i] for j in range(0, len_d, i))

                if len(s) == 1:
                    # print(f"{[ d[j:j+i] for j in range(0, len_d, i) ]}, {d}")
                    res.append(int(d))
                    break

                
print(sum(res))