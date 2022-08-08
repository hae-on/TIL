document = input()
word = input()

start = 0
cnt = 0

while start <= len(document) - len(word):
    if document[start:start+len(word)] == word:
        cnt += 1
        start += len(word)
    else:
        start += 1

print(cnt)