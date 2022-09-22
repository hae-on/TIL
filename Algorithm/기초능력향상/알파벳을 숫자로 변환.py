import sys
sys.stdin = open("input.txt")

word = input()

for s in word:
    print(ord(s)-64, end=" ")
