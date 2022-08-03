N = int(input())
first_sc = []
second_sc =[]
third_sc =[]

for _ in range(N):
    a, b, c = map(int, input().split())
    first_sc.append(a)
    second_sc.append(b)
    third_sc.append(c)

    
for i in range(N):
    score = 0
    if first_sc.count(first_sc[i]) == 1 :
        score += first_sc[i]
    if second_sc.count(second_sc[i]) == 1:
        score += second_sc[i]
    if third_sc.count(third_sc[i]) == 1:
        score += third_sc[i]
    
    print(score)

