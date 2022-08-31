import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

value = 0
asc = []

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        value += arr[i+1]-arr[i]
    else:
        value = 0
    asc.append(value)

print(max(asc))
