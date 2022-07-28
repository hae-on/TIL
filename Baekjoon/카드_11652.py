import sys
sys.stdin = open("input.txt")

N = int(input())

d = {}

for i in range(1, N+1):
    card = int(input())

    if card in d:
        d[card] += 1
    else:
        d[card] = 1

# 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
# 카드 개수 기준 내림차순, 개수 같으면 카드 값 기준 오름차순 (lambda 함수 참고)
sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

#[(1, 3), (2, 2)]
print(sorted_d[0][0])
