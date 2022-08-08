N, M = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(N, M , cards):
    max_total = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                total = cards[i] + cards[j] + cards[k]
            
                if max_total < total <= M:
                    max_total = total
            
                if total == M:
                    return total

    return max_total

print(blackjack(N, M ,cards))