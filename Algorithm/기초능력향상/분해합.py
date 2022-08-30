n = int(input())

result = 0

for i in range(1, n+1):
    result = i

    iValue = str(i)
    for j in range(len(iValue)):
        result += int(iValue[j])

    if result == n:
        print(i)
        break

    if i == n:
        print(0)
