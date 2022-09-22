import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    scores = list(map(int, input().split()))
    score_list = [0] * 101

    for score in scores:
        score_list[score] += 1

    max_ = max(score_list)
    result = []

    for i in range(len(score_list)):
        if score_list[i] == max_:
            result.append(i)

    print(f'#{tc} {max(result)}')
