import sys
sys.stdin = open("input.txt")

K = input()
row = ord(K[0])-96
col = int(K[1])

direction = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for i in direction:
    nx = row + i[0]
    ny = col + i[1]

    if not(0< nx <= 8 and 0< ny <=8):
        continue

    cnt += 1


print(cnt)