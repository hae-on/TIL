import sys
sys.stdin = open("숫자카드게임.txt")

n, m = map(int, input().split())
result = []

for i in range(n):
    card = list(map(int, input().split()))
    result.append(min(card))

print(max(result))
