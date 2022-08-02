import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    result = 0
    max_ = 0

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #무조건 M이 더 크도록 설정
    if N > M :
        N, M = M, N
        A, B = B, A

    max_ = 0

    for i in range(M-N+1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[j+i]

        if tmp > max_:
            max_ = tmp

    print(f'#{tc} {max_}')
