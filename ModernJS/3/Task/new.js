// 1. new A()==new B()가 성립 가능한 함수 A와 B를 만드는 게 가능할까요?

function A() {
  //...
}
function B() {
  //...
}

let a = new A();
let b = new B();

alert(a == b); // true

// 만약 가능하다면, 실행 가능한 예시를 작성해 보세요.
let obj = {};

function A() {
  return obj;
}
function B() {
  return obj;
}

alert(new A() == new B());

// 2. 아래와 같은 세 개의 메서드를 가진 생성자 함수, Calculator를 만들어보세요.
function Calculator() {
  this.read = function () {
    this.a = +prompt("a", 0);
    this.b = +prompt("b", 0);
  };

  this.sum = function () {
    return this.a + this.b;
  };

  this.mul = function () {
    return this.a * this.b;
  };
}

let calculator = new Calculator();
calculator.read();

alert("Sum=" + calculator.sum());
alert("Mul=" + calculator.mul());

// 3. 생성자 함수 Accumulator(startingValue)를 만들어 보세요.
function Accumulator(startingValue) {
  this.value = startingValue;

  this.read = function () {
    this.value += +prompt("값", 0);
  };
}

let accumulator = new Accumulator(1); // 최초값: 1

accumulator.read(); // 사용자가 입력한 값을 더해줌
accumulator.read(); // 사용자가 입력한 값을 더해줌

alert(accumulator.value);
