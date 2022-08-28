import sys
sys.stdin = open("문자열압축.txt")

s = input()
answer = len(s)
for i in range(1, len(s)//2 + 1):
    compressed = ""
    prev = s[0:i]
    cnt = 1
    for j in range(i, len(s), i):
        if prev == s[j:j + i]:
            cnt += 1
        else:
            compressed += str(cnt) + prev if cnt >= 2 else prev
            prev = s[j:j+i]
            cnt = 1
    compressed += str(cnt) + prev if cnt >= 2 else prev
    answer = min(answer, len(compressed))

print(answer)
