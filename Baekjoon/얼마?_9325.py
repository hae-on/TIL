T = int(input())

for _ in range(1, T+1):
    S = int(input())
    N = int(input())

    for _ in range(N):
        q, p = map(int, input().split())
        S += q * p
    
    print(S)