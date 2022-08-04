import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(1, T+1):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])