# 반복문

## for in 반복문

```javascript
  for (const 반복 변수 in 배열 또는 객체) {
    문장
  }
```

## for of 반복문

```javascript
  for (const 반복 변수 of 배열 또는 객체) {
    문장
  }
```

## for 반복문

```javascript
for (let i = 0; i < 반복횟수; i++) {
  문장;
}
```

### for 반복문과 함께 배열 사용하기

```javascript
const list = ['사과', '복숭아', '귤'];

for (let i = 0; i < list.length; i++) {
  console.log(`${i}번째 과일: ${list[i]}`);
}
```

## while 반복문

> 불 표현식이 true면 계속 실행

```javascript
 while (불 표현식){
  문장
 }
```

### while 반복문과 함께 배열 사용하기

```javascript
let i = 0;
const arr = [1, 2, 3, 4, 5];

while (i < arr.length) {
  console.log(i);
  i++;
}
```

## break

> switch 조건문이나 반복문을 벗어날 때 사용

```javascript
 while(true){

 }break
```

## continue

> 반복 작업을 멈추고 처음부터 다시 돌아가 다음 반복 작업 진행

```javascript
for (let i = 0; i < 5; i++) {
  continue;
  console.log(i);
}
```
