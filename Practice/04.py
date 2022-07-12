n = 5
i = 1
result = 1

# while문 곱
while i <= n:
    result *= i
    i += 1
print(result)

result = 1

# for문 곱
for i in range(1, n+1):
    result *= i
print(result)
