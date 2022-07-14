# 배열

> 여러개의 변수를 한 번에 선언해 다룰 수 있는 자료형

## 배열 만들기

`[요소, 요소, 요소 ...]`

## 배열 요소에 접근하기

`배열[인덱스]`

## 배열 요소 개수 확인하기

`배열.length`

## 배열 뒷부분에 요소 추가하기

### push() 메소드를 사용해 배열 뒷부분에 요소 추가하기

`배열.push(요소)`

### 인덱스를 사용해 배열 뒷부분에 요소 추가하기

```javascript
list = [a, b, c];
list[3] = d;
list[list.length] = e;
```

## 배열 요소 제거하기

### 인덱스로 요소 제거하기

`배열.splice(인덱스, 제거할 요소의 개수)`

### 값으로 요소 제거하기

```
const 인덱스 = 배열.indexOf(요소)
배열.splice(인덱스, 1)
```

### 배열 내부에서 특정 값을 가진 요소 모두 제거

```javascript
const list = ['a', 'a', 'b', 'c'];
list.filter((item) => item !== 'a');
-> ['b','c']
```

## 배열의 특정 위치에 요소 추가하기

`배열.splice(인덱스, 0, 요소)`

## 자료의 비파괴와 파괴

### 비파괴

> 처리 후에 원본 내용 변경 x

```javascript
const a = "안녕"
const b = "?"
const c = a + b

console.log(a, b) -> 그대로 "안녕", "?"

```

### 파괴

> 처리 후 원본 내용 변경 o

```javascript
list = ["a", "b"]
list.push("c")

console.log(list) -> ["a","b","c"] 원본 변경
```
