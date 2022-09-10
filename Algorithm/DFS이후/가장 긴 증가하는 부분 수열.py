import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    max_ = 0
    for j in range(i):
        if arr[i] > arr[j] and dp[j] > max_:
            max_ = dp[j]
    dp[i] = max_ + 1
    
print(dp)