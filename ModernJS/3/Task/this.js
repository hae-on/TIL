// 1. 이 객체의 ref에 접근하면 어떤 결과가 발생하고, 그 이유는 뭘까요?
function makeUser() {
  return {
    name: "John",
    ref: this,
  };
}

let user = makeUser();

alert(user.ref.name); // 결과가 어떻게 될까요?
// 에러 발생. this 값을 설정할 땐 객체 정의가 사용되지 않기 때문

// function makeUser() {
//   return {
//     name: "John",
//     ref() {
//       return this;
//     },
//   };
// }

// let user = makeUser();

// alert(user.ref().name); // John

// 2. 계산기 만들기
let calculator = {
  read() {
    this.a = +prompt("입력 1: ", 0);
    this.b = +prompt("입력 2: ", 0);
  },

  sum() {
    return this.a + this.b;
  },

  mul() {
    return this.a * this.b;
  },
};

calculator.read();
alert(calculator.sum());
alert(calculator.mul());

// 3. up, down, showStep을 수정해 아래처럼 메서드 호출 체이닝이 가능하도록 해봅시다.
let ladder = {
  step: 0,
  up() {
    this.step++;
    return this;
  },
  down() {
    this.step--;
    return this;
  },
  showStep: function () {
    // 사다리에서 몇 번째 단에 올라와 있는지 보여줌
    alert(this.step);
    return this;
  },
};

ladder.up().up().down().showStep();
