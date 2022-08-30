na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = []
for i in a:
    if i not in b:
        result.append(i)

result.sort()
print(len(result))

if len(result) != 0:
    print(*result)
