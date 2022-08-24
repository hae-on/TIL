// 1. 다음 각 동작을 한 줄씩, 코드로 작성해보세요.
let user = {};
user.name = "John";
user.surname = "Smith";

user.name = "Pete";

delete user.name;

// 2. 객체에 프로퍼티가 하나도 없는 경우 true, 그렇지 않은 경우 false를 반환해주는 함수 isEmpty(obj)를 만들어 보세요.
function isEmpty(obj) {
  for (let key in obj) {
    return false;
  }
  return true;
}

// 3. const와 함께 선언한 객체를 변경하는 게 가능할까요? 생각을 공유해주세요!
const user = {
  name: "John",
};
// 아래 코드는 에러 없이 실행될까요?
user.name = "Pete";
// 에러 없이 실행 가능, const여도 user는 객체 참조 값을 저장하기 때문

// 4. 모든 팀원의 월급을 합한 값을 구하고, 그 값을 변수 sum에 저장해주는 코드를 작성해보세요.
let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130,
};

sum = 0;
for (let key in salaries) {
  sum += salaries[key];
}

console.log(sum);

// 5. 객체 obj의 프로퍼티 값이 숫자인 경우 그 값을 두 배 해주는 함수 multiplyNumeric(obj)을 만들어보세요.
function multiplyNumeric(obj) {
  for (let key in obj) {
    if (typeof obj[key] == "number") {
      obj[key] *= 2;
    }
  }
}

let menu = {
  width: 200,
  height: 300,
  title: "My menu",
};

multiplyNumeric(menu);

console.log(menu);
