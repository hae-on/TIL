import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    a, b = input().split()
    
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if sorted_a == sorted_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')

