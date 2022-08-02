import sys
sys.stdin = open("input.txt", "r")

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


T = int(input())


for tc in range(1, T+1):
    result = 0
    m1, d1, m2, d2 = map(int,input().split())

    for i in range(m1, m2):
        if m1 == i:
            result += months[i] - d1 + 1
        else:
            result += months[i]
    result += d2

    print(f'#{tc} {result}')

