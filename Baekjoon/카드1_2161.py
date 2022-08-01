card = []
N = int(input())

for i in range(1, N+1):
    card.append(i)

while len(card) != 1:
    # 앞에서부터 순서대로 빠짐 맨 위 버리기
    print(card.pop(0))
    card.append(card.pop(0))

print(*card)