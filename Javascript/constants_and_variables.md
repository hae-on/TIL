# 상수와 변수

## 상수

> 항상 같은 수

`const 이름 = 값`

1. 한 파일에서 한 번만 선언 가능
2. 선언할 때 값을 반드시 지정
3. 한 번 선언된 상수의 자료 변경 불가

## 변수

> 변할 수 있는 수

`let 이름 = 값`

1. 특정한 이름의 변수는 한 파일에서 한 번만 선언 가능

## 변수에 적용 가능한 연산자

### 복합 대입 연산자

| 복합 대입 연산자 | 설명               |
| ---------------- | ------------------ |
| +=               | 기존 변수에 더함   |
| -=               | 기존 변수에 뺌     |
| \*=              | 기존 변수에 곱함   |
| /=               | 기존 변수에 나눔   |
| %=               | 기존 변수의 나머지 |

### 증감 연산자

| 증감 연산자 | 설명                    |
| ----------- | ----------------------- |
| 변수++      | 기존 값에 1 더함 / 후위 |
| ++변수      | 기존 값에 1 더함 / 전위 |
| 변수--      | 기존 값에 1 뺌 / 후위   |
| --변수      | 기존 값에 1 뺌 / 전위   |

## undefined 자료형

### 상수와 변수로 선언하지 않은 식별자

```javascript
  type(a) -> undefined
```

### 값이 없는 변수

```javascript
  let a -> undefined
```