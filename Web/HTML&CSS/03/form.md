## form

> 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

### input 유형 - 일반

- text: 일반 텍스트 입력
- password: 입력 시 값이 보이지 않고 문자를 특수 기호로 표현
- email: 이메일 형식이 아닌 경우 form 제출 불가
- number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
- file: accept 속성을 활용하여 파일 타입 지정 가능

### input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목 작성
- 동일 항목에 대하여는 name 지정하고 선택 항목에 value 지정
  - checkbox: 다중 선택
  - radio: 단일선택

### input 유형 - 기타

- 다양한 종류의 input을 위한 picker 제공
  - color: color picker
  - date: date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden: 사용자에게 보이지 않는 input
