N = int(input())

body = []

for i in range(1, N+1):
    x, y = map(int, input().split())
    # body.append(x, y) -> TypeError: list.append() takes exactly one argument (2 given)
    body.append((x, y))

for i in body:
    # 0등은 없기 때문에 1등부터 시작
    cnt = 1
    for j in body:
        if i != j:
            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1

    print(cnt, end=" ")
