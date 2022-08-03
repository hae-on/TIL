import sys
sys.stdin = open("input.txt")

N = int(input())

for _ in range(1, N+1):
    A, B = map(int, input().split())

    money = 0

    if A == 1:
        money += 5000000
    elif 1 < A <= 3:
        money += 3000000
    elif 3 < A <= 6:
        money += 2000000
    elif 6 < A <= 10:
        money += 500000
    elif 10 < A <= 15:
        money += 300000
    elif 15 < A <= 21:
        money += 100000
    else:
        money+= 0

    if B == 1:
        money += 5120000
    elif 1 < B <= 3:
        money += 2560000
    elif 3 < B <= 7:
        money += 1280000
    elif 7 < B <= 15:
        money += 640000
    elif 15 < B <= 31:
        money += 320000
    else:
        money += 0
    
    print(money)