word = 'banana'


def find_in_str(x, word):
    for i, item in enumerate(word):
        if item == x:
            return i
    return -1


print(find_in_str('a', word))


# 추가문제
word = 'HappyHacking'

for idx, char in enumerate(word):
    if char == 'a':
        print(idx, end=" ")
