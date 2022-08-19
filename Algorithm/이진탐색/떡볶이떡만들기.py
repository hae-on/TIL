import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)


result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid

    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
