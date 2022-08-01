T = int(input())

for i in range(1, T+1):
    N = input()
    stack = []
    answer = 'YES'

    for j in N:
        if j == '(':
            stack.append('(')
        else :
            if len(stack) == 0:
                answer = 'NO'
            else: 
                stack.pop()

    if len(stack) > 0 :
        answer = 'NO'
    
    print(answer)