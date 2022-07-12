numbers = [3, 10, 20]
result = 0

# 리스트 전체 합
for i in numbers:
    result += i

# 리스트 갯수
cnt = 0
for i in numbers:
    cnt += 1

print(int(result/cnt))
