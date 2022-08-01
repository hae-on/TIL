import sys
sys.stdin = open("input.txt")

status = input()
stack=[]

while status != '고무오리 디버깅 끝':
    if status == '문제':
        stack.append('문제')
    elif status == '고무오리':
        if len(stack) != 0 :
            stack.pop()
        else:
            stack.append('문제')
            stack.append('문제')
    status = input()

if len(stack) != 0:
    print('힝구')
else:
    print('고무오리야 사랑해')