## Branch basic commands

### 1. 브랜치 생성 및 이동

`(master) $ git checkout -b feature/about `<br>
`(feature/about) $`

### 2. 작업 완료 후 commit

`(feature/about) $ touch about.txt`<br>
`(feature/about) $ git add .`<br>
`(feature/about) $ git commit -m "Add about.txt"`<br>
`$ git log --oneline`

### 3. master에 병합

`(master) $ git merge feature/test`

### 4. branch 삭제

`$ git branch -d feature/test`
