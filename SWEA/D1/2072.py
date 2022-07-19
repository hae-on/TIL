# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    nums = list(map(int, input().split()))
    odd_nums = [n for n in nums if n % 2 == 1]
    print(f'#{i} {sum(odd_nums)}')
