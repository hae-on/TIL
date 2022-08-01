import sys
sys.stdin = open("input.txt")

N = int(input())
milk_list = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if milk_list[i] == cnt % 3:
        cnt += 1

print(cnt)
