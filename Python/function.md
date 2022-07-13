## 함수

- Decomposition 기능 분해, 재사용 가능
- Abstraction 추상화, 복잡한 내용을 숨기고 기능에 집중

### 함수

- 특정한 기능을 하는 코드의 조각
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편하게 사용

```python
def 이름(parameter) :
return
```

### 함수의 결과값

- 함수는 반드시 값을 하나만 return한다.
- 함수는 return과 동시에 종료

### 함수의 입력

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때, 넣어주는 값
  - 필수 Argument : 반드시 전달
  - 선택 Argument : 값이 전달하지 않아도 되는 경우 기본 값이 전달

### 함수의 범위

- built-in-scope
- global scope
- local scope

### 함수 응용

- map
  - 순회 가능한 데이터 구조의 모든 요소에 함수 적용하고, 그 결과를 map object로 반환
