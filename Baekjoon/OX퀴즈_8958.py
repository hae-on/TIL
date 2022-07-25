T = int(input())

for tc in range(1, T+1):
    quiz = list(input())
    cnt = 0
    total = 0
    for ox in quiz:
        if ox == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
