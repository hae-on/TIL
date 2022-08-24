import sys
sys.stdin = open("문자열뒤집기.txt")

n = input()

cnt0 = 0
cnt1 = 0

num = int(n[0])

if num == 1:
    cnt1 += 1
else:
    cnt0 += 1

for i in range(1, len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '1':
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))
