N = int(input())

result = 0

for i in range(1, N+1):
    # 245 -> 245 + 2 + 4 + 5
    result = i

    iValue = str(i)
    for j in range(len(iValue)):
        result += int(iValue[j])

    if result == N:
        # result = break 안하면 198 207 출력. 제일 최소값을 구하는 것이므로 값이 나오면 바로 break
        print(i)
        break

    # 생성자가 없는 경우 0 출력
    if i == N:
        print(0)
