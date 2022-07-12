word = 'happy!'

# while문 길이 출력
cnt = 0
while word[cnt:]:
    cnt += 1

print(cnt)

# for문 길이 출력
cnt = 0
for i in word:
    cnt += 1

print(cnt)

# for문 index 길이 출력
for idx in range(len(word)):
    idx += 1

print(idx)
