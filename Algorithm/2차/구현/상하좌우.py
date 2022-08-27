import sys
sys.stdin = open("상하좌우.txt")

N = int(input())
plan = list(input().split())

direction = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

x = 1
y = 1

for i in plan:
    dx, dy = direction[i]

    nx = x + dx
    ny = y + dy

    if not(0 < nx < N and 0 < ny < N):
        continue

    x = nx
    y = ny

print(x, y)
