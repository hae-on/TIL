# import sys
# sys.stdin = open("input.txt", "r")

N = int(input())

game = ['3', '6', '9']

for i in range(1, N+1):
    x = str(i)
    cnt = 0
    for j in range(len(x)):
        if x[j] in game:
            cnt += 1
    if cnt > 0:
        x = '-' * cnt
    print(x, end=" ")
