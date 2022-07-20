# Object

- 파이썬은 모두 객체(object)로 이루어져 있다.
- 객체는 특정 타입(Class)의 인스턴스(Instance)이다.
  - 123, 900, 5는 모두 int의 인스턴스
  - 'hello', 'bye'는 모두 string의 인스턴스

## 객체

- 객체의 특징
  - 타입(type): 어떤 연산자와 조작이 가능한가?
  - 속성(attribute): 어떤 상태(데이터)를 가지는가?
  - 조작법(method): 어떤 행위(함수)를 할 수 있는가?

## 객체 지향 프로그래밍

> 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- 장점
  - 프로그램을 유연하고 변경이 용이하게 만듦
  - 소프트웨어 개발과 보수 간편하게 함
  - 직관적인 코드 분석 가능

## OOP 기초

```python
 # 클래스 정의
 class MyClass:
  # 인스턴스 생성
  my_instance = MyClass()
  # 메서드 호출
  my_instance.my_method()
  # 속성
  my_instance.my_attribute()
```

- 객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성한다.

- 클래스와 인스턴스

  - 클래스: 객체들의 분류
  - 인스턴스: 하나하나의 실체/예

- 객체 비교하기
  - ==
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은)경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
  - is
    - 동일한(identical)
    - 두 변수가 동일한 객체를 가리키는 경우 True

```python
  a = [1,2,3]
  b = [1,2,3]
  print(a == b, a is b) => True, False
```

```python
  a = [1,2,3]
  b = a
  print(a == b, a is b) => True, True
```

## 인스턴스

- 인스턴스 변수
  - 인스턴스가 개인적으로 가지고 있는 속성
  - 각 인스턴스들의 고유한 변수
- 생성자 메소드에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

- 인스턴스 메소드

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
  - 클래스 내부에 정의되는 메소드의 기본
  - 호출 시, 첫번째 인자로 인스턴스 자기자신이 전달됨

- self

  - 인스턴스 자기자신
  - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫번째 인자로 정의
    - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자(constructor) 메소드

  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - \_\_init\_\_메소드 자동 호출

- 소멸자(destructor) 메소드
  - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드

```python
  class Person:

    def __init__(self, name):
      self.name = name

    def greeting(self):
      print(f'안녕하세요, {self.name}입니다.')

  jimin = Person('지민')
  jimin.greeting()

  iu = Person('지은')
  iu.greetion()
```

## 클래스

- 클래스 속성
  - 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
  - 클래스 선언 내부에서 정의
  - <classname>.<anme>으로 접근 및 할당

```python
  class Circle:
    pi = 3.14

  c1 = Circle()
  c2 = Circle()

  print(Circle.pi) #3.14
  print(c1.pi) #3.14
  print(c2.pi) #3.14
```

- 인스턴스와 클래스 간의 이름 공간(namespace)

  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

- 클래스 메소드
  - 클래스가 사용할 메소드
  - @classmethod 데코레이터(함수를 어떤 함수로 꾸며서 새로운 기능을 부여)를 사용하여 정의
  - 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

```python
class MyClass

  @classmethod
  def class_method(cls, arg1, ...)
```

- 스태틱 메소드
  - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
  - 속성을 다루지 않고 단지 기능(헹동)만을 하는 메소드를 정의할 때 사용
  - @staticmethod 데코레이터를 사용하여 정의
  - 호출 시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/수정 불가)

```python
class MyClass

  @staticmethod
  def class_method(arg1, ...)
```

### 전체 메소드 정리

```python
 class MyClass:

  def method(self):
    return 'instance method', self

  @classmethod
  def classmethod(cls):
    return 'class method', cls

  @staticmethod
  def staticmethod():
    return 'static method'
```

## 객체 지향의 핵심개념

- 추상화
- 상속
  - 두 클래스 사이 부모-자식 관계를 정립하는 것
  - 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
  - 상속 관련 함수와 메소드
    - issubclass(class, classinfo):class가 classinfo의 subclass면 True
    - super():자식 클래스에서 부모 클래스를 사용하고 싶은 경우

```python
  class Person:
    def __init(self, name, age):
      self.name = name
      self.age = age

  class Student(Person):
    def __init__(self, name, age, email):
      #Person 클래스
      super().__init__(name, age)
      self.email = email
```

- 다형성
  - 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
  - 메소드 오버라이딩
    - 상속 받은 메소드를 재정의
    - 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
    - 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용

```python
 class Person:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')

  #자식 클래스
  class Professor(Person):
    def talk(self):
      print(f'{self.name}일세.')

  #자식 클래스
  class Student(Person):
    def talk(self):
      super().talk()
      print(f'저는 학생입니다.')

  p1 = Professor('김교수')
  p1.talk() #김교수일세.

  s1 = Student('이학생')
  s1.talk() # 반갑습니다. 이학생입니다.
            # 저는 학생입니다.

```

- 캡슐화
  - 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스 차단
  - 파이썬에서 기능상으로 존재하지 않지만, 관용적으로 사용되는 표현이 있음
  - 접근 제어자 종류
    - Public Access Modifier
      - 언더바 없이 시작하는 메소드나 속성
      - 어디서나 호출이 가능, 하위 클래스 override 허용
    - Protected Access Modifier
      - 언더바 1개로 시작하는 메소드나 속성
      - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
    - Private Access Modifier
      - 언더바 2개로 시작하는 메소드나 속성
      - 본 클래스 내부에서만 사용이 가능
