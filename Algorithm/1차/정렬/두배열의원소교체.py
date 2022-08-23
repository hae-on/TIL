import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b = sorted(list_b, reverse=True)

for i in range(K):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        break

print(sum(list_a))
