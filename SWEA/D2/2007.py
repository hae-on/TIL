# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    string = input()
    answer = 0

    for i in range(1, len(string)):
        if(string[i] == string[0]):
            if(string[:i] == string[i:i*2]):
                answer = i
                break

    print(f'#{tc} {answer}')
