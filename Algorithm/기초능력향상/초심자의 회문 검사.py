import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = input()
    if word == word[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
