import sys
sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    score = list(input())
    sum_ = 0
    cnt = 0
    for i in score:
        if i == 'O':
            cnt += 1
            sum_ += cnt
        else:
            cnt = 0

    print(sum_)
