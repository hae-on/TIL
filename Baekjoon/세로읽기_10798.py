import sys
sys.stdin = open("input.txt")

words = []
length = []
result = ""

for i in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

for i in range(max(length)):
    for j in range(5):
        # result += words[j][i] or ''로 작성하니 런타임 오류
        print(length[j])
        if i < length[j]:
            result += words[j][i]

print(result)
