// 아래 코드를 실행하면, 의도한 대로 문자열(str)에 프로퍼티(test)를 추가할 수 있을까요?
// 만약 가능하다면 얼럿 창엔 무엇이 출력될까요?
let str = "Hello";

str.test = 5; // (*)

console.log(str.test);

// TypeError: Cannot create property 'test' on string 'Hello'
// vscode: undefined

// 풀이
// 1. undefined (비 엄격 모드)
// 2. An error (엄격 모드)

// str의 프로퍼티에 접근하려 하면 "래퍼 객체"가 만들어집니다.
// 엄격 모드에선 래퍼 객체를 수정하려 할 때 에러가 발생합니다.
// 비 엄격 모드에선 에러가 발생하지 않습니다.
// 래퍼 객체에 프로퍼티 test가 추가되죠.
// 그런데 래퍼 객체는 바로 삭제되기 때문에 마지막 줄이 실행될 땐 프로퍼티 test를 찾을 수 없습니다.
