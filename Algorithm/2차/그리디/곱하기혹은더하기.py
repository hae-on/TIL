import sys
sys.stdin = open("곱하기혹은더하기.txt")

# 0과 1일때는 더한다.
# 나머지는 곱한다.

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
