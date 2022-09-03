import sys
sys.stdin = open("input.txt")

document = input()
word = input()

cnt = 0
index = 0

while index <= len(document) - len(word):
    if document[index:index+len(word)] == word:
        cnt += 1
        index += len(word)
    else:
        index += 1

print(cnt)
