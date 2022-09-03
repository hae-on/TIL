import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
card = list(map(int, input().split()))

sum_ = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] <= m:
                sum_.append(card[i] + card[j] + card[k])

print(max(sum_))
