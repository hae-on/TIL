# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q
    if W > R:
        B += (W - R) * S

    if A > B:
        print(f'#{i} {B}')
    else:
        print(f'#{i} {A}')
