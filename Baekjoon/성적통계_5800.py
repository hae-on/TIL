K = int(input())

for i in range(K):
    class_ = input().split()

    N = int(class_[0])
    scores = list(map(int, class_[1::]))
    scores.sort()

    max_ = max(scores)
    min_ = min(scores)
    gap = []

    for j in range(len(scores)-1):
        gap.append(scores[j+1]-scores[j])

    print(f'Class {i+1}')
    print(f'Max {max_}, Min {min_}, Largest gap {max(gap)}')
    