import sys
sys.stdin = open("input.txt")

N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

d = {}

for i in card1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in card2:
    if i in d:
        print(d[i], end=" ")
    else:
        print(0, end=" ")
