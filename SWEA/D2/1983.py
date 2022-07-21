import sys
sys.stdin = open("input.txt", "r")

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    total = []

    for _ in range(N):
        M, F, T = map(int, input().split())
        data = M * 0.35 + F * 0.45 + T * 0.2
        total.append(data)

    K_score = total[K-1]
    total.sort(reverse=True)

    value = N // 10
    result = total.index(K_score) // value

    print(f'#{tc} {score[result]}')
