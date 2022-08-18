import sys
sys.stdin = open("input.txt")

N = int(input())
list_ = []

for _ in range(N):
    list_.append(int(input()))

arr = sorted(list_, reverse=True)

print(*arr)
