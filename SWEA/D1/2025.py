# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
answer = 0

for i in range(0, n+1):
    answer += i

print(answer)
