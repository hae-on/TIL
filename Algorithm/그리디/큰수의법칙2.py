import sys
sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

max_ = arr[N-1]
second_max = arr[N-2]

max_cnt = M // (K + 1) * K
max_cnt += M % (K + 1)

answer = 0
answer += max_cnt * max_
answer += (M - max_cnt) * second_max

print(answer)