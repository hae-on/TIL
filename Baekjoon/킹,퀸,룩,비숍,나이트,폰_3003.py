import sys
sys.stdin = open("input.txt")

chess = [1, 1, 2, 2, 2, 8]

d_chess = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i]-d_chess[i], end=" ")