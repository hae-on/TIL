import sys
sys.stdin = open("input.txt")

names = input().split('-')

first_alp = list(map(lambda x: x[0], names))

print(''.join(first_alp))

