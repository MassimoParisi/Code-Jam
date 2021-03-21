import numpy as np

T = int(input())
for t in range(T):
    N = int(input())
    M = np.array([list(map(int, input().split())) for _ in range(N)])
    k = np.trace(M)
    r = sum(len(set(r)) < N for r in M)
    c = sum(len(set(c)) < N for c in M.T)
    print("Case #{}: {} {} {}".format(t+1, k, r, c))
    