import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

noHear = set()
for _ in range(N):
    noHear.add(input())

noSee = set()
for _ in range(M):
    noSee.add(input())

noHearSee = sorted(list(noHear & noSee))

print(len(noHearSee))

for i in noHearSee:
    print(i)
