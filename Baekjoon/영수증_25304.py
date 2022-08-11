import sys
sys.stdin = open("input.txt")

X = int(input())
N = int(input())

sum_ = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum_ += a * b

if sum_ == X:
    print('Yes')
else:
    print('No')