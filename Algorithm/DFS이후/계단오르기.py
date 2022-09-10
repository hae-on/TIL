import sys
sys.stdin = open("input.txt")

n = int(input())
list_ = []
dp = []

for _ in range(n):
   list_.append(int(input()))


if n == 1:
    print(list_[0])
elif n == 2:
    print(max(list_[0]+list_[1], list_[1]))


dp.append(list_[0])
dp.append(max(list_[0]+list_[1], list_[1]))
dp.append(max(list_[0]+list_[2], list_[1]+list_[2]))

for i in range(3, n):
    dp.append( max(list_[i-1]+list_[i]+dp[i-3],list_[i]+dp[i-2]))

print(dp[-1])