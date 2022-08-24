import sys
sys.stdin = open("큰수의법칙.txt")

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)

first_num = arr[0]
second_num = arr[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_num
        m -= 1
    if m == 0:
        break
    result += second_num
    m -= 1


print(result)
