import sys
sys.stdin = open("input.txt")

N = int(input())
d = {}

for i in range(1, N+1):
    book = input()

    if book in d:
        d[book] += 1
    else:
        d[book] = 1

best = max(d.values())
bestseller = []

for i in d:
    if d[i] == best:
        bestseller.append(i)

bestseller.sort()
print(bestseller[0])
