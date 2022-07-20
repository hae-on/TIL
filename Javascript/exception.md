# 구문 오류와 예외

## 오류의 종류

- 프로그램 실행 전에 발생하는 오류 : 구문오류
- 프로그램 실행 중에 발생하는 오류 : 예외, 런타임 오류

### 구문 오류

```javascript
  console.log('hi
```

### 예외

```javascript
console.lg('hi');
```

## 기본 예외 처리

> 조건문을 사용해서 예외가 발생하지 않게 만드는 것

## 고급 예외 처리

> try catch finally 구문 사용

```javascript
try {
  //예외가 발생할 가능성이 있는 코드
} catch (exception) {
  //예외가 발생했을 때 실행할 코드
} finally {
  //무조건 실행할 코드
}
```

finally 코드가 없다면 중간에 return이나 break, continue 키워드를 만나면 결과가 달라짐

# 예외 처리 고급

## 예외 객체

> try catch 구문을 사용할 때 catch의 괄호 안에 입력하는 식별자가 예외 객체

```javascript
try {
} catch (예외객체) {}
```

## 예외 강제 발생

```javascript
throw 문자열
throw new Error 문자열
```
