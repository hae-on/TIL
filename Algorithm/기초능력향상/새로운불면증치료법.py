import sys
sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = [0] * 10
    x = 1
    while 0 in arr:
        num = str(n * x)
        for j in range(len(num)):
            arr[int(num[j])] += 1
        x += 1

    print(f'#{i} {num}')
