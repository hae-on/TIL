#pypy3 제출
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
list_ = []

for _ in range(N):
    list_.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    sum_ =0

    for r in range(i, x+1):
        for c in range(j, y+1):
            sum_ += list_[r][c]

    print(sum_)

