import sys
sys.stdin = open("input.txt")

for _ in range(3):
    num = input()
    answer = 0

    for i in range(7):
        cnt = 1
        for j in range(i+1, 8):
            if num[i] == num[j]:
                cnt += 1
            else:
               break
        answer = max(answer, cnt)
    
    print(answer)