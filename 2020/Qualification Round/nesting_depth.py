T = int(input())
for t in range(T):
    r = input()        #current row
    y = ["Case #{}: ".format(t+1)]
    curr = int(r[0])
    for _ in range(curr):
        y.append("(")
    y.append(str(curr))
    for i in range(1, len(r)):
        nxt = int(r[i])
        diff = curr - nxt
        if diff >= 0:
            for _ in range(diff):
                y.append(")")
        else:
            for _ in range(abs(diff)):
                y.append("(")
        y.append(str(nxt))
        curr = nxt
    for _ in range(curr):
        y.append(")")
    print("".join(el for el in y))
    y = ""
        