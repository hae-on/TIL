## 조건문

- 참 / 거짓을 판단할 수 있는 조건식과 함께 사용

```python
if <expression> :
  # Run this Code block
else:
  # Run this Code block
```

### 예시

```python
num = int(input())
if num % 2 == 1 :
  print('홀수')
else :
  print('짝수')
```

## 복수 조건문

```python
if <expression> :
  # Run this Code block
elif:
   # Run this Code block
else:
    # Run this Code block
```

### 에시

```python
dust = int(input())
if dust > 150:
  if dust >300 :
    print('실외 활동을 자제하세요.')
   print('매우 나쁨')
elif dust > 80 :
  print('나쁨')
elif dust >30 :
  print('보통')
else :
  if dust < 0 :
    print('음수 값입니다.')
  else :
     print('좋음')
```

### 조건 표현식

```python
num = -10

if num >=0
  value = num
else
  value = -num
print(num, value)
```

`value = num if num >=0 else -num`
