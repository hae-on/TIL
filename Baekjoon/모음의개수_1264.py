import sys
sys.stdin = open("input.txt")

vowel = ['a', 'e' , 'i', 'o', 'u']
sentence = input().lower()

while sentence != '#':
    cnt = 0
    for i in sentence:
        if i in vowel:
            cnt += 1
    print(cnt)
    sentence = input().lower()
