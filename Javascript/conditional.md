# if 조건문

## if 조건문

> 불 표현식의 값이 true면 실행, false면 미실행

```javascript
if(표현식){
  실행할 문장
}
```

## if else 조건문

```javascript
if(표현식){
  참일 떄 실행할 문장
} else {
  거짓일 때 실행할 문장
}
```

## 중첩 조건문

> 조건문 안에 조건문 중첩

```javascript
  if(표현식){
    if(표현식2){
      표현식2 참일 때 실행할 문장
    } else {
      표현식2 거짓일 때 실행할 문장
      }
    } else {
      if(표현식3){
        표현식3 참일 때 실행할 문장
      } else {
        표현식3 거짓일 때 실행할 문장
      }
    }
```

## if else if 조건문

```javascript
if (표현식) {
  문장;
} else if (표현식) {
  문장;
} else {
  문장;
}
```

# switch 조건문과 짧은 조건문

## switch 조건문

```javascript
  switch (자료) {
    case 조건 A:
      break
    case 조건 B:
      break
    default:
      break
  }
```

## 조건부 연산자

`불 표현식 ? 참일 때 결과 : 거짓일 때 결과`

## 짧은 연산자

### 논리합 연산자를 사용한 짧은 조건문

`불 표현식 || 불 표현식이 거짓일 때 실행할 문장`

### 논리곱 연산자를 사용한 짧은 조건문

`결과가 거짓인 불 표현식 && 불 표현식이 참일 때 실행할 문장`
