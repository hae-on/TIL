num = int(input())
cnt = 0
x = 665

while cnt != num:
    x += 1
    if str(x).count('666'):
        cnt += 1

print(x)