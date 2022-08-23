import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

answer = 0

for i in range(N):
    cards = list(map(int, input().split()))
    
    max_card = min(cards)

    answer = max(answer, max_card)

print(answer)