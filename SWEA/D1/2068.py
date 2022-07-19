# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


def solution(nums):
    return str(max(nums))


for i in range(1, T+1):
    nums = list(map(int, input().split()))
    print(f'#{i} {solution(nums)}')
