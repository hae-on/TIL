# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    max_N = N_list[-1]
    profit = 0

    for x in range(N-2, -1, -1):
        if N_list[x] >= max_N:
            max_N = N_list[x]
        else:
            profit += max_N - N_list[x]

    print(f'#{i} {profit}')
