import sys
sys.stdin = open("1_단어공부.txt")

word = input().upper()
# ['S', 'P', 'I', 'M']
list_ = list(set(word))
cnt = []

for i in list_:
    cnt.append(word.count(i))

# count method를 사용해 최댓값이 중복되는 지 확인한다. (중복되는 갯수가 뜸)
# 1이상이면 최댓값이 똑같은 것이 여러개 있다는 뜻
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    # max(cnt)의 index를 찾고 이를 list_에서 찾아준다.
    print(list_[cnt.index(max(cnt))])
