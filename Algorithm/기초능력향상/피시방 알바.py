n = int(input())
num = map(int, input().split())

seat = [0] * 101
cnt = 0

for i in num:
    if seat[i] == 0:
        seat[i] += 1
    else:
        cnt += 1

print(cnt)
