import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    location, wrong_word = input().split()
    location = int(location)
    print(wrong_word[:location-1] + wrong_word[location:])
