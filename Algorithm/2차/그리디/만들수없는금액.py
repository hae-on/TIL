import sys
sys.stdin = open("만들수없는금액.txt")

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

sum_coin = 1

for i in coin:
    if i > sum_coin:
        break
    sum_coin += i

print(sum_coin)
