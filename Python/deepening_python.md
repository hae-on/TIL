## 추가 문법

### List Comprehension

> 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성

[<expression> for <변수> in <iterable>] <br>
[<expression> for <변수> in <iterable> if <조건식>]

- 1~3의 세제곱의 결과가 담긴 리스트 만들기

```python
  [number**3 for number in range(1, 4)]
```

### Dictionary Comprehension

> 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

{key: value for <변수> in <iterable>} <br>
{key: value for <변수> in <iterable> if <조건식>}

- 1~3의 세제곱의 결과가 담긴 딕셔너리 만들기

```python
  {number: number**3 for number in range(1,4)}
```

### lambda [parameter] : 표현식

- 람다함수
  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용가능

# 파이썬 표준 라이브러리

- 패키지 설치
  - pip install SomePackage
  - pip install SomePackage==1.xx
  - pip install SomePackage>=1.xx
- 패키지 삭제
  - pip uninstall SomePackage
- 패키지 목록 및 특정 패키지 정보
  - pip list
  - pip show SomePackage
- 패키지 freeze
  - pip freeze
- 패키지 관리하기
  - pip freeze > requirements.txt
  - pip install -r requirements.txt
