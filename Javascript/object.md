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
