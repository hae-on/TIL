# 객체의 기본

## 객체

> 이름과 값으로 구성된 속성을 가진 자바스크립트의 기본 데이터 타입

`키 : 값`

### 객체 접근

```javascript
const fruits = {
  사과: apple,
  복숭아: peach,
  블루베리: blueberry,
};
```

```javascript
fruits['사과'] = apple;
fruits['복숭아'] = peach;
fruits.블루베리 = blueberry;
```

## 속성과 메소드

> 객체 내부에 있는 값 = 속성

### 속성과 메소드 구분하기

> 객체의 속성 중 함수 자료형인 속성 = 메소드

### 메소드 내부에서 this 키워드 사용하기

> 자기 자신이 가진 속성 표시할 때 this 사용

```javascript
const man = {
  이름: '홍길동',
  행동: function (action) {
    console.log(this.이름 + 은 + action + 를 합니다.);
  },
};

man.행동('공부')
```

## 동적으로 객체 속성 추가/제거

> 객체를 처음 생성한 후에 속성을 추가하거나 제거하는 것

### 동적으로 객체 속성 추가하기

```javascript
const man = {};
man.이름 = '홍길동';
man.성별 = '남자';

console.log(JSON.stringify(man, null, 2));
// {
//  "이름" : "홍길동",
// "성별" : "남자",
// }
```

### 동적으로 객체 속성 제거하기

`delete 객체.속성`

```javascript
delete man.성별;
```

## 메소드 간단 선언 구문

```javascript
  const man ={
    name: '홍길동',
    study(과목){
      console.log(this.name + 은 + 과목 + 을 공부합니다.)
    }
  }
  man.study('과학')
```

# 객체의 속성과 메소드 사용하기

## 객체 자료형

> 속성과 메소드를 가질 수 있는 모든 것은 객체

- 배열
- 함수

## 기본 자료형

> 실체가 있는 것 중에 객체가 아닌 것

- 숫자
- 문자열
- 불

## 기본 자료형을 객체로 선언하기

`const 객체 = new 객체 자료형 이름()`

```javascript
new Number(123);
new String('hi');
```

## 프로토타입으로 메소드 추가하기

```javascript
  객체 자료형 이름.prototype.메소드 이름 = function(){

  }
```

## Number 객체

### 숫자 N번째 자릿수까지 출력하기: toFixed()

```javascript
const a = 123.45667;
a.toFixed(2); //123.45
```

### NaN과 Infinity 확인하기: isNaN(), isFinite()

```javascript
const a = Number('hi');
Number.isNaN(a); //true

const a = 10 / 0;
Number.isFinite(a); //false
```

## String 객체

### 문자열 양쪽 끝의 공백 없애기: trim()

```javascript
const a = '   안녕   ';
a.trim(); //안녕
```

### 문자열을 특정 기호로 자르기: split()

## JSON 객체

> 자바스크립트의 객체처럼 자료를 표현하는 방식

```javascript
  "name":"홍길동",
  "age":40
```

- 값을 표현할 때는 문자열, 숫자, 불 자료형만 사용 가능 (함수 사용 불가)
- 문자열 반드시 큰 따옴표
- 키에도 따옴표사용

- JSON.stringify(): 객체를 문자열로 변환
- JSON.parse(): 문자열을 객체로 변환

## Math 객체

> 수학과 관련된 기본적인 연산

# 객체와 배열 고급

## 속성 존재 여부 확인

> 객체 내에 어떤 속성이 있는지 확인

```javascript
const object = {
  name: '홍길동',
  age: 40,
};

if (object.name !== undefined) {
  console.log('name이 있습니다.');
} else {
  console.log('name이 없습니다.');
}

if (object.gender !== undefined) {
  console.log('gender가 있습니다.');
} else {
  console.log('gender가 없습니다.');
}
```

### 더 짧은 예시

```javascript
object.name || console.log('name이 있습니다.');
object.gender || console.log('gender가 있습니다.');
```

### 기본 속성 지정

```javascript
object.name = object.name || '이름 미정';
object.gender = object.gender || '성별 미정';
```

## 배열 기반의 다중 할당

`[식별자, 식별자, 식별자, ...] = 배열`

```javascript
let [a, b] = [1, 2];
console.log(a, b); //1 2

let arr = [1, 2, 3, 4, 5];
const [a, b, c] = arr;
console.log(a, b, c); //1 2 3
```

## 객체 기반의 다중 할당

`{속성 이름, 속성 이름} = 객체`
`{식별자 = 속성 이름, 식별자 = 속성 이름} = 객체`

```javascript
const object = {
  name: '홍길동',
  age: 40,
};

const { name, age } = object;
console.log(name, age); // 홍길동 40

const { a = name, b = age } = object;
console.log(a, b); // 홍길동 40
```

## 배열 전개 연산자

- 얕은 복사
- 깊은 복사
  - `[...배열]`
  - `[...배열, 자료, 자료, 자료 ]`

## 객체 전개 연산자

`{...객체}`

### 전개 연산자를 사용한 객체 요소 추가

`{...객체, 자료, 자료, 자료}`

```javascript
const man = {
  name: '홍길동',
  age: 40,
};

const man2 = {
  ...man,
  name: '고길동',
  age: 35,
  gender: man,
};

console.log(JSON.strigify(man)); //{"name":"홍길동", "age":40}
console.log(JSON.strigify(man2)); //{"name":"고길동", "age":35, "gender":"man"}
```

### 만약 전개 부분을 바꾼다면?

```javascript
const man = {
  name: '홍길동',
  age: 40,
};

const man2 = {
  name: '고길동',
  age: 35,
  gender: man,
  ...man,
};

console.log(JSON.strigify(man)); //{"name":"홍길동", "age":40}
console.log(JSON.strigify(man2)); //{"name":"홍길동", "age":40, "gender":"man"}
```
