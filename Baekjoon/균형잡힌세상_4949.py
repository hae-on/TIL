import sys
sys.stdin = open("input.txt")

while True:
    s = input()
    stack=[]
    flag = 1

    if s =='.':
        break
    
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
        else:
            continue
    
    if flag and not stack:
        print('yes')
    else:
        print('no')
