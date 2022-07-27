word = input()
CAMBRIDG = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in CAMBRIDG:
    word = word.replace(i, '').strip()

print(word)
