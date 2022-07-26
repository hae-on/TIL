import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    li = [0] * 101

    for score in scores:
        li[score] += 1

    max_value = max(li)
    result = []

    for i in range(len(li)):
        if li[i] == max_value:
            result.append(i)

    print(f'#{tc} {max(result)}')
