n = 10

list_ = []
for i in range(n):
    num = int(input())
    cal_num = num % 42
    list_.append(cal_num)

print(len(set(list_)))
