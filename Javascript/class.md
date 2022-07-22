# 클래스의 기본 기능

## 추상화

> 프로그램에 필요한 요소만 사용해서 객체를 표현하는 것

## 클래스 선언하기

```javascript
  class 클래스 이름{

  }
```

### 인스턴스 생성

`new 클래스 이름()`

- 클래스 : 이전에 살펴보았던 객체를 만드는 함수와 비슷한 것 ex) 붕어빵 틀
- 인스턴스(객체) : 이전에 만들었던 객체를 만드는 함수로 만든 객체와 비슷한 것 ex) 실체화된 붕어빵

### 클래스 선언, 인스턴스 생성 예시

```javascript
class Man {}

const man = new Man();

const manlist = [
  new Man()
  new Man()
  new Man()
]
```

- 클래스 이름은 대문자로 지정하는 것이 약속

## 생성자

> new Man() 열고 닫는 기호, 객체가 생성될 때 호출되는 생성자라는 이름의 함수

```javascript
 class 클래스 이름 {
  constructor() {
    //생성자 코드
  }
 }
```

### 생성자 함수와 속성, 메소드 추가한 예시

```javascript
class Exam {
  constructor(이름, 국어, 수학, 영어) {
    this.이름 = 이름;
    this.국어 = 국어;
    this.수학 = 수학;
    this.영어 = 영어;
  }

  getSum() {
    return this.국어 + this.수학 + this.영어;
  }

  getAverage() {
    return this.getSum() / 3;
  }

  const exam = []
    exam.push(new Exam('홍길동', 34, 54, 65))
    exam.push(new Exam('고길동', 36, 66, 83))

}
```

# 클래스의 고급 기능

## 상속

```javascript
   class 클래스 이름 extends 부모 클래스 이름 {

   }
```

## private 속성과 메소드

```javascript
  class 클래스 이름 {
    #속성 이름
    #메소드 이름(){

    }
  }
```

## 게터와 세터

- 게터: 메소드처럼 속성 값을 확인할 때 사용
- 세터: 메소드처럼 속성에 값을 지정할 때 사용

```javascript
  class 클래스 이름 {
    get 이름() {return 값}
    set 이름 (value) {}
  }
```

## static 속성과 메소드

> 인스턴스를 만들지 않고 사용할 수 있는 속성과 메소드

```javascript
  class 클래스 이름{
    static 속성 = 값
    static 메소드() {

    }
  }
```

```javascript
 클래스 이름.속성
 클래스 이름.메소드()
```
