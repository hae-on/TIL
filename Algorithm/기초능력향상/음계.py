arr = list(map(int, input().split()))

list_ = []
for i in range(1, 9):
    list_.append(i)


if arr == list_:
    print('ascending')
elif arr == list(reversed(list_)):
    print('descending')
else:
    print('mixed')
