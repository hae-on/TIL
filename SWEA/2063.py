# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
nums = list(map(int, input().split()))

nums.sort()
len_num = T // 2

print(nums[len_num])
