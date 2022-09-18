import sys
sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t+1):
    arr = list(map(int, input().split()))
    sum_ = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 1:
            sum_ += arr[j]

    print(f'#{i} {sum_}')
