// 1. 아래 코드의 결과를 예측해 보세요.
alert( null || 2 || undefined ); //2

// 2. 아래 코드의 결과를 예측해 보세요.
alert( alert(1) || 2 || alert(3) ); // 1 2
// alert메서드는 undefined를 반환

// 3. 아래 코드의 결과를 예측해 보세요.
alert( 1 && null && 2 ); // null

// 4. 아래 코드의 결과를 예측해 보세요.
alert( alert(1) && alert(2) ); // 1 undefined

// 5. 아래 코드의 결과를 예측해 보세요.
alert( null || 2 && 3 || 4 ); // 3
// AND 연산자 &&의 우선순위는 ||보다 높습니다. -> null || 3 || 4

// 6. age(나이)가 14세 이상 90세 이하에 속하는지를 확인하는 if문을 작성하세요.
let age

if (age >= 14 && age <=90) {
alert('age살 입니다.')
}

// 7. age(나이)가 14세 이상 90세 이하에 속하지 않는지를 확인하는 if문을 작성하세요.
if (!(age >= 14 && age <=90)) {
alert('age살 입니다.')
} 
if(age<14 || age>90){
  alert('age살 입니다.')
}

// 8. 아래 표현식에서 어떤 alert가 실행될까요?
if (-1 || 0) alert( 'first' );
if (-1 && 0) alert( 'second' );
if (null || -1 && 1) alert( 'third' );
//first, third

// 9. 프롬프트(prompt) 대화상자를 이용해 간이 로그인 창을 구현해보세요.
let userName = prompt('이름을 입력해주세요', '')

if(userName == 'Admin'){
  let password = prompt('비밀번호를 입력해주세요.', '')

  if (password == 'TheMaster'){
    alert('환영합니다.')
  }else if(password == '' || password == null){
    alert('취소되었습니다.')
  }else{
    alert('인증에 실패하였습니다.')
  }
} else if (userName == '' || userName == null){
  alert('취소되었습니다.')
} else{
  alert('인증되지 않은 사용자입니다.')
}
