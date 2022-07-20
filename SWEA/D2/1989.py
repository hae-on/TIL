import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def palindrome(word):
    return int(word == word[::-1])


for tc in range(1, T+1):
    word = str(input())
    print(f'#{tc} {palindrome(word)}')
