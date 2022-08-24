import sys
sys.stdin = open("모험가길드.txt")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

team = 0
cnt = 0

for i in arr:
    cnt += 1
    if cnt >= i:
        team += 1
        cnt = 0

print(team)
