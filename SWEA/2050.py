# import sys
# sys.stdin = open("input.txt", "r")

str = input()

for char in str:
    print(ord(char)-64, end=" ")
