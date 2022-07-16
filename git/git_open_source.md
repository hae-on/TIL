## 기본 명령어

- ls: 폴더 안에 있는 내용 확인
- cd: 현재 폴더 경로 이동
- pwd: print working directory 현재 폴더 경로 확인
- mv: 파일명 변경(또는 파일 경로 이동)
- touch: 빈파일 만들기

## git 명령어

- git log --oneline | wc -l : 수정이 몇 번 일어났는가
- git shortlog -sn | nl : 수정을 많이한 랭킹
- git shortlog -sn --mnist(폴더이름) | nl :mnist 파일을 가장 많이 개발한 사람
- git shortlog --after=2018-01-01(날짜정보) --before=(날짜정보)|-sn --mnist(폴더이름) | nl :mnist 파일을 최근에 가장 많이 개발한 사람
- git show 해시값 : 히스토리 내역 확인

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

$ git config --global --unset credential.helper
$ git config --system --unset credential.helper

## git rebase

(1) 팀프로젝트 URL 등록 <br>
git remote add upstream "오픈 소스 프로젝트 URL"<br>
(2) 최신 히스토리를 가져온다 => 내부 브랜치 자동생성<br>('upstream/master') <br>
git fetch upstream master <br>
(3)베이스를 최신화 시킨다. <br>
git rebase upstrem/master<br>
(4)강제로 fork한 프로젝트를 갱신 <br>
git push origin fix-mnist(브랜치 이름) --force <br>
