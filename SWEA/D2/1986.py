# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    n = int(input())

    start = 1
    for x in range(2, n+1):
        if x % 2 == 0:
            start -= x
        else:
            start += x
    print(f'#{i} {start}')
