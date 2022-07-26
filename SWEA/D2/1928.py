# SW 사이트 인코딩 오류
from base64 import b64decode

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()
    answer = b64decode(word).decode('UTF-8')
    print(f'#{tc} {answer}')
