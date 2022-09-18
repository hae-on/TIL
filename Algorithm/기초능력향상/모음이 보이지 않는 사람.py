import sys
sys.stdin = open("input.txt")

vowels = ['a', 'e', 'i', 'o', 'u']

t = int(input())

for i in range(1, t+1):
    word = input()
    new_word = ""
    for j in word:
        if j not in vowels:
            new_word += j
    print(f'#{i} {new_word}')
