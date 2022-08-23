import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
list_ = list(map(int, input().split()))

arr.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in list_:
    result = binary_search(arr, i, 0, N-1)

    if result == None:
        print('no', end=" ")
    else:
        print('yes', end=" ")
