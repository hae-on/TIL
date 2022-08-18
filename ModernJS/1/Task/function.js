// 1. else 삭제해도 동일하게 작동?
function checkAge(age) {
  if (age > 18) {
    return true;
  } else {
    // ...
    return confirm("보호자의 동의를 받으셨나요?");
  }
}
// -> 동일하게 작동

// 2. if문을 사용하지 않고 동일한 동작을 하는 함수를 한 줄에 작성해보세요.
// 2-1. 물음표 연산자 ?를 사용하여 본문을 작성
function checkAge(age) {
  return age > 18 ? true : confirm("보호자의 동의를 받으셨나요?");
}
// 2-2. OR 연산자 ||를 사용하여 본문을 작성
function checkAge(age) {
  return age > 18 || confirm("보호자의 동의를 받으셨나요?");
}

// 3. a와 b 중 작은 값을 반환해주는 함수, min(a,b)을 만들어보세요.
function min(a, b) {
  return Math.min(a, b);
}

// 4. x의 n제곱을 반환해주는 함수, pow(x,n)를 만들어보세요.
function pow(x, n) {
  return Math.pow(x, n);
}

let x = prompt("x를 입력해주세요", "");
let n = prompt("n를 입력해주세요", "");

if (n < 1) {
  alert("자연수를 입력해주세요");
} else {
  alert(pow(x, n));
}
