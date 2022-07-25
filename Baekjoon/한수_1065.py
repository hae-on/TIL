N = int(input())


def check(N):
    han = 0
    for i in range(1, N+1):
        N_list = list(map(int, str(i)))
        if i < 100:
            han += 1
        elif N_list[0] - N_list[1] == N_list[1] - N_list[2]:
            han += 1
    return han


print(check(N))
