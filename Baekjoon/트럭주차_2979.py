import sys
sys.stdin = open("input.txt")

A, B, C = map(int, input().split())

# 입력으로 주어지는 시간은 1과 100사이 이다.
time = [0] * 100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1

# print(time)
sum_ = 0
for i in time:
    if i == 1:
        sum_ += A * 1
    elif i == 2:
        sum_ += B * 2
    elif i == 3:
        sum_ += C * 3

print(sum_)
    