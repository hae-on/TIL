from pprint import pprint
import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    sum_ = 0

    for r in range(i, x+1):
        for c in range(j, y+1):
            sum_ += arr[r][c]

    print(sum_)
