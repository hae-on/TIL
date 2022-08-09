import sys
sys.stdin = open("input.txt")

R, C = map(int, input().split())
C0 = C1 = C2 = C3= C4 = 0

space = []
for _ in range(R):
    space.append(input())


for i in range(R - 2 + 1): 
    for j in range(C - 2 + 1):
        tmp = ''
        for x in range(2):
            for y in range(2):
                tmp += space[i+x][j+y]
        if "#" in tmp:
            continue
        else:
            car = tmp.count('X')
            if car == 0:
                C0 += 1
            elif car == 1:
                C1 += 1
            elif car == 2:
                C2 += 1
            elif car == 3:
                C3 += 1
            else:
                C4 += 1

print(C0)
print(C1)
print(C2)
print(C3)
print(C4)

