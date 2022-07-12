## 반복문

> 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

### 반복문의 종류

- while 문
- for 문
- 반복 제어

### while

- while문은 조건식이 참인 경우 반복적으로 코드를 실행
  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록 실행
  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
  - 무한 루프 하지 않도록 종료 조건 반드시 필요

### 예제

```python
n =0
result =0
user_input = int(input())

while n <= user_input:
  result += n
  n+= 1
  print(result)>
```

### for문

- for문은 시퀀스를 포함한 순회 가능한 객체 요소를 모두 순회함
  - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음

```python
for <변수명> in <iterable>:
  # Code block
```

### 문자열 순회

```python
chars = input()
for idx in range(len(chars)):
print(chars[idx])
```

### 딕셔너리 순회

- 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john':80, 'eric':90}
for name in grades:
  print(name)
  #john, eric 출력
```

### 반복문 제어

- break : 반복문 종료
- continue : continue 이후의 코드 블록 수행하지 않고, 다음 반복 수행
- for-else : 끝까지 반복문 실행한 후에 else 문 실행 (break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음)
