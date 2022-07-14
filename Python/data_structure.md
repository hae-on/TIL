`타입.메서드()`

# 메서드(methods)

## 문자열

### 문자열 탐색

- find(x)

  - x의 첫 번째 위치를 반환, 없으면 -1 반환

- index(x)
  - x의 첫 번째 위치를 반환, 없으면 오류 발생

### 문자열 변경

- replace(old, new[,count])

  - 바꿀 대상 글자를 새로운 글자로 바꿔서 변환
  - count를 지정하면, 해당 개수만큼만 시행

- strip([chars])

  - 특정한 문자들을 지정하면,
  - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
  - 문자열을 지정하지 않으면 공백을 제거함

- split(sep=None, maxsplit=-1)

  - 문자열을 특정한 단위로 나눠 리스트로 반환
    - sep이 None이거나 지정되지 않으면 연속된 공백 문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
    - maxsplit이 -1인 경우에는 제한이 없음

- 'separator'.join([iterable])

  - 반복가능한 컨테이너 요소들을 separator(구분자)로 합쳐 문자열로 반환

    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생

---

## 리스트

### 값 추가 및 삭제

- append(x)

  - 리스트에 값을 추가함

- extend(iterable)

  - 리스트에 iterable의 항목을 추가함

- insert(i, x)

  - 정해진 위치 i에 값을 추가함

- remove(x)

  - 리스트에서 값이 x인 것 삭제

- pop(i)

  - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
  - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

- clear()

  - 모든 항목을 삭제함

### 탐색 및 정렬

- index(x)

  - x 값을 찾아 해당 index 값을 반환

- count(x)

  - 원하는 값의 개수를 반환함

- sort()

  - 원본 리스트를 정렬함. None 반환
  - sorted 함수와 비교 (정렬된 리스트를 반환, 원본 변경 없음)

- reverse()

  - 순서를 반대로 뒤집음

---

## 딕셔너리

### 조회

- get(key[,default])

  - key를 통해 value를 가져옴
  - keyError가 발생하지 않으며, default 값을 설정할 수 있음 (기본 : None)

  ### 추가 및 삭제

- pop(key[,default])

  - key가 딕셔너리에 있으면 제거하고 해당 값을 반환
  - 그렇지 않으면 default를 반환
  - default 값이 없으면 keyError

- update([other])

  - 값을 제공하는 key, value로 덮어
