import sys
sys.stdin = open("input.txt")

n= 5

words = []
length = []
result = ""

for _ in range(n):
    word = input()
    words.append(word)
    length.append(len(word))

for i in range(max(length)):
    for j in range(n):
        if i < length[j]:
            result += words[j][i]

print(result)


