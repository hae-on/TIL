croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for alphabet in croatia:
    word = word.replace(alphabet, '#')

print(len(word))
