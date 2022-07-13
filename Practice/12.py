word = input()

result = word

for char in word:
    if char in 'a':
        result = result.replace(char, '')

print(result)
