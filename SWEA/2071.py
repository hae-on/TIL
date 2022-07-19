# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    number = map(int, input().split())
    sum_n = sum(n for n in number)
    print(f'#{i} {round(sum_n/10)}')
