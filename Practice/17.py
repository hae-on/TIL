word = 'banana'

for char in word:
    change_upper_ord = int(ord(char)-32)
    print(chr(change_upper_ord), end="")
