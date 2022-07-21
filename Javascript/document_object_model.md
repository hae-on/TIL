# 문서 객체 조작하기

> HTML 페이지에 있는 h1, div 등을 HTML에서는 요소라고 부르는데, 자바스크립트에서는 문서 객체라고 부름

## DOMContentLoaded 이벤트

> 문서 객체 조작할 때 사용

```javascript
document.addEventListener('DOMContentLoaded', () => {
  //문장
});
```

## 문서 객체 가져오기

```javascript
document.head;
document.body;
document.title;
```

### head나 body 내부에 만든 다른 요소 사용

```javascript
document.querySelector(선택자); //요소 하나 추출
document.querySelectorAll(선택자); //요소 여러개 추출, forEach()를 사용해 반복 돌림
```

## 글자 조작하기

- 문서 객체.textContent : 입력된 문자열 그대로 넣음
- 문서 객체.innerHTML : 입력된 문자열 HTML 형태로 넣음

## 속성 조작하기

- 문서 객체.setAttribute(속성 이름, 값) : 특정 속성에 값 지정
- 문서 객체.getAttribute(속성 이름) : 특정 속성 추출

## 스타일 조작하기

> style 속성 사용

```javascript
h1.style.backgroundColor;
h1.style['backgroundColor'];
h1.style['background-color'];
```

## 문서 객체 생성하기

`document.createElement(문서 객체 이름)` <br>

## 문서 객체 이동하기

문서를 어떤 문서 아래 추가할 지 지정해줘야 함 <br>
`부모 객체.appendChild(자식 객체)` <br>
이는 문서 객체를 이동할 때 사용하기도 함

## 문서 객체 제거하기

`부모 객체.removeChild(자식 객체)`
`문서 객체.parentNode.removeChild(문서 객체)`

## 이벤트 설정하기

`문서 객체.addEventListener(이벤트 이름, 콜백 함수)` <br>
여기서 콜백 함수는 이밴트 리스너 혹은 이벤트 핸들러라고 부름

## 이벤트 제거하기

`문서 객체.removeEventListener(이벤트 이름, 이벤트 리스너)`

# 이벤트 활용

## 이벤트 모델

> 이벤트를 연결하는 방법

표준 이벤트 모델

```javascript
document.body.addEventListener('keyup', () => {
  //문장
});
```

## 키보드 이벤트

- keydown : 키가 눌릴 때 사용
- keypress : 키가 입력되었을 때 사용
- keyup : 키보드에서 키가 떨어질 때 사용

## 이벤트 발생 객체

상황에 따라서 이벤트 리스너 내부에서 변수에 접근할 수 없는 경우 있음 <br>

해결 방안 <br>

- event.currentTarget 속성 사용
  - () => {}와 function(){} 형태 모두 사용 가능
- this 키워드 사용
  - function(){} 형태만 사용 가능

## 글자 입력 양식 이벤트

> 사용자로부터 어떠한 입력을 받을 때 사용하는 요소를 입력 양식이라 부름

- 드롭다운
- 체크 박스
- 라디오 버튼

## 기본 이벤트 막기

`preventDefault()`
