import sys
sys.stdin = open("왕실의나이트.txt")

w = input()
row = ord(w[0])-96
col = int(w[1])

direction = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for i in direction:
    nx = row + i[0]
    ny = col + i[1]

    if not(0 < nx <= 8 and 0 < ny <= 8):
        continue

    cnt += 1

print(cnt)
