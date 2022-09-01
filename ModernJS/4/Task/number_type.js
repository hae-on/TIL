// 1. 사용자에게 두 수를 입력받고, 두 수의 합을 출력해주는 스크립트를 작성해보세요.

let a = +prompt("a?", "");
let b = +prompt("b?", "");

console.log(a + b);

// 2. 위 예시와 유사한 아래의 경우, 6.35가 6.4가 아닌 6.3으로 반올림되는 이유는 무엇일까요?
// -> 정밀도 손실 때문에 실제로는 6.35보다 작다.

// 어떻게 하면 6.35를 제대로 반올림할 수 있을까요?
alert((6.35 * 10).toFixed(20));

// 3. 사용자가 유효한 숫자형 값을 입력할 때까지 계속 입력받는 함수 readNumber 를 만들어보세요.
function readNumber() {
  let num;

  do {
    num = prompt("수를 입력해주세요", "");
  } while (!isFinite(num));

  if (num === null || num === "") return null;

  return +num;
}

alert(readNumber());

// 4. This loop is infinite. It never ends. Why?
let i = 0;
while (i != 10) {
  i += 0.2;
}
// -> 0.2를 더해도 정확히 10이 되지 않기 때문

// 5. Now if we add min, the possible interval becomes from min to max.
function random(min, max) {
  return min + Math.random() * (max - min);
}
