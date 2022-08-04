import sys
sys.stdin = open("input.txt")

T = int(input())

for i in range(1, T+1):
    line = list(input().split())
    for j in line:
        print(j[::-1], end=" ")
    print()