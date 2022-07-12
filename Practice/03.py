n = 10
i = 1
result = 0

# while문 사용 합
while i <= n:
    result += i
    i += 1

print(result)

result = 0

# for문 사용 합
for i in range(1, n+1):
    result += i

print(result)
