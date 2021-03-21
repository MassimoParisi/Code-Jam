def check(s, e, arr) -> bool:
    for el in arr:
        if max(s, el[0]) < min(e, el[1]):
            return False
    return True

T = int(input())
cameron = []
jamie = []
for t in range(T):
    cameron.clear()
    jamie.clear()
    y = []
    N = int(input())
    for _ in range(N):
        S, E = map(int, input().split(" ")) # start, end
        if y == "IMPOSSIBLE": continue
        if check(S, E, cameron): 
            y.append("C")
            cameron.append((S,E))
        elif check(S, E, jamie):
            y.append("J")
            jamie.append((S,E))
        else:
            y = "IMPOSSIBLE"
    print("Case #{}: {}".format(t+1, "".join(y)))


#4
#3
#360 480
#420 540
#600 660    