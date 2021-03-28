T = int(input())
for t in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    Ls = sorted(L)
    count = 0
    for i in range(len(L)-1):
        j = L.index(Ls[i])
        count += j - i + 1
        L = L[:i] + L[i:j+1][::-1] + L[j+1:]
    print("Case #{}: {}".format(t+1, count))
