# Git

버전을 통해 코드를 관리하는 도구



# SCM & VCS

- SCM(Source Code Management) : 코드 관리
- VCS(Version Control System) : 버전 관리



# Git 명령어

> **Git** 은 폴더 단위로 프로젝트/코드를 관리

## 1. `git init`

initialize, initiate

- `git`으로 코드 관리 시작
  1. `(master)`라는 표시가 프롬프트에 표시됨
  2. `.git` 폴더가 생성됨



## 2. `git status`

**가장 중요한 명령어**

- `git`의 상태를 출력

  1. `git init` 직후

     ```shell
     On branch master
     
     No commits yet
     
     nothing to commit (create/copy files and use "git add" to track)
     ```

     - No commits yet : 아직 commit이 없다 (버전 == 스냅샷 == 특정상태 == 저장)
     - nothing to commit : commit 할 것이 없다.

  2. `a.txt` 파일 추가 후

     ```shell
     On branch master
     
     No commits yet
     
     Untracked files:
     	(use "git add <file>..." to include in what will be committed)
     		a.txt
     		
     nothing added to commit but untracked filed present (use "git add" to track)
     ```

     - untracked files : 추적되지 않는 파일이 있다.
     - nothing added to commit but untracked filed present : 커밋할 파일은 없지만, 추적되지 않은 파일은 없다.

  3. `git add a.txt` 후

     ```shell
     On branch master
     
     No commits yet
     
     Changes to be committted:
     	(use "get rm --cached <file>..." to unstage)
     		new file:	a.txt
     ```

     - changes to be committed : commit될 준비마친 파일이 있다.

  4. `git commit -m "first commit"` 후

     ```shell
     On branch master
     nothing to commit, working tree clean
     ```
     
- nothing to commit : commit 할 것이 없다.
     - working tree clean : 작업 폴더가 비어있다.



## 3. `git add [파일명]`

`git`이 스냅샷을 찍기 위해 추적하는 리스트에 파일을 추가



## 4. `git commit -m "[커밋 메세지]"`

`git`을 통해 스냅샷을 찍음 (== 버전을 만듦 == 현재 상태를 저장)

- `-m` : message
  1. 언제 찍었는지
  2. 누가 찍었는지 : 이름, 이메일
  3. 메세지
  4. commit hash



## 5. `git log`

`git`으로 지금까지 저장한 커밋들의 로그를 출력

- `git log --online` : 한 줄로 커밋을 출력
- `git log -[숫자]` : 입력된 숫자만큼 최신 커밋부터 역순으로 출력



## 6. `git restore -- staged [파일명]`

staging area에 추가된 파일을 복원