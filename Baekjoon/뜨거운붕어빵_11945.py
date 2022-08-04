import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

for _ in range(1, N+1):
    print(input()[::-1])
