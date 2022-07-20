# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
result = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for x in range(M):
                for y in range(M):
                    tmp += fly[i+x][j+y]
            if tmp > kill:
                kill = tmp
    result.append(kill)

for a in range(T):
    print(f'#{a + 1} {result[a]}')
