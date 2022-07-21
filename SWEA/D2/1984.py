# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


def avg_score(N):
    total = sum(N)-max(N)-min(N)
    avg_total = round(total / (len(N)-2))
    return avg_total


for tc in range(1, T+1):
    N = list(map(int, input().split()))
    print(f'#{tc} {avg_score(N)}')
