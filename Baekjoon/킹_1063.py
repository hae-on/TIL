import sys
sys.stdin = open("input.txt")

directions = { 
    "R": (0, 1),
    "L": (0, -1), 
    "B": (1, 0), 
    "T": (-1, 0), 
    "RT": (-1, 1), 
    "LT": (-1, -1), 
    "RB": (1, 1), 
    "LB": (1, -1),
}

k, s, n = input().split()

kx, ky = 8 - int(k[1]), ord(k[0]) - 65 
sx, sy = 8 - int(s[1]), ord(s[0]) - 65

for _ in range(int(n)):
    loc = input()
    dx, dy = directions[loc]

    # 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
    if not(0 <= kx + dx < 8 and 0 <= ky + dy < 8) :
        continue

    kx = kx + dx
    ky = ky + dy
    
    if (kx, ky) == (sx, sy):
        if not(0 <= sx + dx < 8 and 0 <= sy + dy < 8):
            # stone이 밖으로 나가면 king의 움직임을 이전으로 되돌린다.
            kx = kx - dx
            ky = ky - dy
            continue
        sx = sx + dx
        sy = sy + dy

print(chr(65 + ky) + str(8 - kx))
print(chr(65 + sy) + str(8 - sx))
