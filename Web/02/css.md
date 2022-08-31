# CSS position

> 문서 상에서 요소 위치 지정

- static (기준 위치)
- relative (상대 위치)
- absolute (절대 위치)
- fixed (고정 위치)
- sticky (스크롤에 따라 fixed로 변경)

# flexbox

## 기본 개념

- 1차원 레이아웃 모델로 설계 (한 번에 하나의 차원만 다룸)

## flexbox의 두 개의 축

### 주축

Row
Row-reverse
Column
Column-reverse

### 교차축 (주축에 수직)

Row, Row-reverse라면 교차축은 열 방향
Column, Column-reverse라면 교차축은 행 방향

### flex 컨테이너

flexbox가 놓여있는 영역을 flex 컨테이너라고 부름

### flex 속성

- 배치설정
  - flex-direction
  - flex-wrap
- 공간나누기
  - justify-content (main axis)
  - align-content (cross axis)
- 정렬
  - align-items (모든 아이템을 cross axis기준으로)
  - align-self(개별 아이템)
