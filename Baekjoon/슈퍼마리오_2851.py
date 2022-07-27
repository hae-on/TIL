mushrooms = []

for _ in range(10):
    mushrooms.append(int(input()))

sum_ = 0
tmp = 0

for mushroom in mushrooms:
    sum_ += mushroom
    if sum_ == 100:
        print(sum_)
        break
    elif sum_ > 100:
        tmp = sum_-mushroom
        # 100에 더 가까운 수를 골라야 함
        if 100-tmp >= sum_-100:
            print(sum_)
            break
        else:
            print(tmp)
            break
# 점수를 다 더해도 100이 안되는 경우
else:
    print(sum_)
