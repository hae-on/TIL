import sys
sys.stdin = open("input.txt")

N = int(input())

list_ = []
for _ in range(N):
    list_.append(input().split())

list_ = sorted(list_, key=lambda s: int(s[1]))

for s in list_:
    print(s[0], end=" ")
