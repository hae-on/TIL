import sys
sys.stdin = open("input.txt")

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print(f'#{i+1} {a//b} {a % b}')
