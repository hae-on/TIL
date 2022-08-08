T = int(input())

for _ in range(T):
    cnt = 0
    N, M = map(int, input().split())

    for i in range(N, M+1):
        j = str(i)
        cnt += j.count('0')
    
    print(cnt)