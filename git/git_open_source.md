# Git open Source 강의 필기

## 기본 명령어

- ls: 폴더 안에 있는 내용 확인
- cd: 현재 폴더 경로 이동
- pwd: print working directory 현재 폴더 경로 확인
- mv: 파일명 변경(또는 파일 경로 이동)
- touch: 빈파일 만들기

## Git 명령어

- git log --oneline | wc -l : 수정이 몇 번 일어났는가
- git shortlog -sn | nl : 수정을 많이한 랭킹
- git shortlog -sn --mnist(폴더이름) | nl :mnist 파일을 가장 많이 개발한 사람
- git shortlog --after=2018-01-01(날짜정보) --before=(날짜정보)|-sn --mnist(폴더이름) | nl :mnist 파일을 최근에 가장 많이 개발한 사람
- git show 해시값 : 히스토리 내역 확인 (해시값은 git log --oneline하면 나옴)
- git log --reverse : 옛날것부터 소스파일 수정 내역 보기

## commit message

"수정 내역들을 한줄씩 요약해서 보자" <br>
commit message "수정의 이유를 작성한다" <br>

- Fix: 잘못된 것을 고친 것
- Improve: 원래 잘 되던 건데 개선한 것 (ex 10초에서 5초)
- Add: 없던 기능, 옵션 추가할 때
- Support: 윈도우 -> 리눅스
- Refactor: 코드를 재배치
- Remove: 필요 없는 것을 제거

## 다른(사람) GitHub 계정과의 충돌방지

git config --global --unset credential.helper <br>
git config --system --unset credential.helper

## 나노 편집기 사용하기

git config --global core_editor nano

## 브랜치

- 브랜치 생성: git checkout -b <브랜치명>
- 브랜치 삭제: git checkout <이동할 브랜치명> -> git branch -D <삭제할 브랜치명>

## Git 추가 명령어

- add 명령 취소: git reset
- commit 명령 취소: git reset --hard HEAD\~숫자 (HEAD\~1은 가장 위에서 첫번째 내용 삭제)
- 라이센스 서명 commit: git commit -sm "커밋 내용"
- commit 수정: git commit --amend

## git rebase

1. 팀프로젝트 URL 등록
   git remote add upstream "오픈 소스 프로젝트 URL"
2. 최신 히스토리를 가져온다 => 내부 브랜치 자동생성('upstream/master')
   git fetch upstream master
3. 베이스를 최신화 시킨다.
   git rebase upstrem/master
4. 강제로 fork한 프로젝트를 갱신
   git push origin fix-mnist(브랜치 이름) --force

- git rebase -i --root
- 해당 줄에 edit으로 바꾸고 control+O, Enter, control+X
- git log --oneline 누르고 되감기 되었는지 확인
- git rebase --continue 다시 풀어주기

## 실습

1. 가장 오래된 역사부터 두번째 commit 이후에 새로운 커밋 3개 넣기

- git rebase -i -root
- 편집기에서 2번째 commit edit으로 변경 후 저장
- touch hello_1.txt && git add hello_1.txt && git commit "Add hello_1.txt" 커밋 3개 등록
- git rebase --continue

2. 중간에 새로 생긴 3개 commit 1개로 합치기

- git rebase -i --root
- 편집기에서 해당 commit edit으로 변경 후 저장
- git reset --soft HEAD~1 (hard는 파일도 삭제, soft는 commit 정보만 삭제)
- git status로 상태 확인
- git commit --amend
- git rebase --continue

3. 프로젝트의 최초 commit부터 3개 찾아보기

- git log --oneline --reverse | head -3 <br>
  (git log --oneline --reverse -3하면 최근 3개가 뒤집어서 출력)
