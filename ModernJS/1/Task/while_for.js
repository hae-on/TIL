// 1. 아래 코드를 실행했을 때 얼럿 창에 마지막으로 뜨는 값은 무엇일까요? 이유도 함께 설명해보세요.
let i = 3;

while (i) {
  alert( i-- );
}
// 1
// 3에서부터 하나씩 빠지다가 while(0)이 되면 종료

// 2. while 반복문이 순차적으로 실행될 때마다 얼럿 창에 어떤 값이 출력될지 예상해보세요.
// 아래 두 예시는 같은 값을 출력할까요?
let j = 0;
while (++i < 5) alert( i ); // 1, 2, 3, 4
let k = 0;
while (i++ < 5) alert( i ); // 1, 2, 3, 4, 5

// 3. for 반복문이 순차적으로 실행될 때마다 얼럿 창에 어떤 값이 출력될지 예상해보세요.
// 아래 두 예시는 같은 값을 출력할까요?
for (let i = 0; i < 5; i++) alert( i ); //0, 1, 2, 3, 4
for (let i = 0; i < 5; ++i) alert( i ); //0, 1, 2, 3, 4

// 4. for 반복문을 이용하여 2부터 10까지 숫자 중 짝수만을 출력해보세요.
for(let i=2; i<11; i++){
  if(i % 2 == 0){
    alert(i)
  }
}

// 5. for 반복문을 while 반복문으로 바꾸되, 동작 방식에는 변화가 없도록 해보세요. 출력 결과도 동일해야 합니다.
for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}

i = 0
while(i<3){
  alert( `number ${i}!` );
  i++
}

// 6. 사용자가 유효한 값을 입력할 때까지 프롬프트 창 띄우기
let num 
do{
  num = prompt('100보다 큰 수를 입력하세요' , 0);
} while (num <= 100 && num)

// 7. 2부터 n까지의 숫자 중 소수만 출력해주는 코드를 작성해봅시다.
let n = 10;

prime:
for (let i = 2; i <= n; i++) { 

  for (let j = 2; j < i; j++) { 
    if (i % j == 0) continue prime; 
  }

  alert( i ); 
}