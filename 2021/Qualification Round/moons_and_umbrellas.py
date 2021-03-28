T = int(input())
for t in range(T):
    data = input().split()
    X = int(data[0])
    Y = int(data[1])
    S = str(data[2]).replace('?', '')
    cost = 0
    i = 0
    while(i < len(S)):
        if (S[i] == 'C') and (i+1 != len(S)) and (S[i+1] == 'J'): cost += X
        elif (S[i] == 'J') and (i+1 != len(S)) and (S[i+1] == 'C'): cost += Y 
        i += 1
    print("Case #{}: {}".format(t+1, cost))