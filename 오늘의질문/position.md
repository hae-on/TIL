## [CSS] Position의 종류와 각 Position의 효과를 작성하세요.

1. static

- HTML elements는 기본적으로 static
- 작성된 문서의 일반적인 흐름을 따름
- top, bottom, left right 속성에 영향 받지 않음
- 문서 상 위치: 유지

2. relative

- static 위치(원래 위치)를 기준으로 상대적 위치 설정
- top, bottom, left right 속성을 적용하면, 요소의 시작 위치가 변경됨
- 문서 상 위치: 유지

3. absolute

- 문서의 흐름과 상관없이, 가장 가까운 position 요소를 기준으로 배치
  - 부모 or 조상 요소 중, position 값이 설정된(static X), 가장 가까운 요소
  - 부모 or 조상에 position 값을 가진 요소가 없는 경우: viewport 기준
- top, bottom, left right 속성을 적용하면, 요소의 시작 위치가 변경됨
- 문서 상 위치: 유지X
  - 일반적 문서 흐름에서 제거
  - 아래 있는 요소가 해당 자리를 차지

4. fixed

- 문서의 흐름과 상관없이, viewport를 기준으로 배치
- top, bottom, left right 속성을 적용하면, 요소의 시작 위치가 변경됨
- 문서 상 위치: 유지X
  - 일반적 문서 흐름에서 제거
  - 아래 있는 요소가 해당 자리를 차지

5. sticky

- 기본적으로 static
- 화면이 스크롤 되어, static 위치를 유지할 수 없으면, fixed

——————————————

<top, bottom, left, right>

- top: 기준점 ~ 요소 시작점의 위쪽 거리
- bottom: 기준점 ~ 요소 시작점의 아래쪽 거리
- left: 기준점 ~ 요소 시작점의 왼쪽 거리
- right: 기준점 ~ 요소 시작점의 오른쪽 거리
