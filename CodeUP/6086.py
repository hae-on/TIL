n = int(input())
cnt = 0
result = 0

while True:
    result += cnt
    cnt += 1
    if result >= n:
        break

print(result)
