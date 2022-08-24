import sys
sys.stdin = open("볼링공고르기.txt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

list_ = [0] * 11
result = 0

for i in arr:
    list_[i] += 1

for i in range(1, m+1):
    n -= list_[i]
    result += list_[i] * n

print(result)
