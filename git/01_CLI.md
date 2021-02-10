# CLI

Command Line Interface

커맨드(명령어)를 통해 작동하는 인터페이스

<-> GUI(Grapic User Interface, 보통의 프로그램)



# GUI vs CLI

- GUI(Graphic User Interface) : 일반적으로(일반인이) 컴퓨터를 다루는 방식 (그래픽 중심)
  - 마우스 중심
- CLI : 개발자들이 다루는 방식
  - 명령어 중심



# 기초 명령어

### (1) `pwd`

- `pwd` (print working directoy) : 현재 디렉토리의 경로
- `~`(home directory) : 홈 디렉토리 (git bash 처음 열면 나오는 기본 폴더)



### (2) `ls`

* `ls` (list) : 해당 디렉토리의 내용 출력



### (3) `cd`

* `cd [폴더명]` (change directory) :  디렉토리 변경 (폴더명 자동 완성은 tab 키)
  * `..` : 상위 디렉토리로 이동
  * `.` : 현재 디렉토리로 이동
  * `/` : 루트 디렉토리로 이동
  * `~` : 홈 디렉토리로 이동 (cd 뒤에 아무 것도 없으면 홈 디렉토리로 이동)



### (4) `mkdir` 

* `mkdir [폴더명]` (make directory) : 디렉토리 생성



### (5) `rm`

* `rm [파일명]` (remove) : 파일 삭제
* `rm -r [폴더명]` (remove recursively) : 폴더 삭제



### (6) `touch`

- `touch [파일명]` : 파일 생성



### (7) `cp`

- `cp [파일명] [위치]` (copy) : 파일 복사
- `cp -r [폴더명] [위치]` : 폴더 복사



### (8) mv

- `mv` (move) : 파일 또는 폴더명 변경
- `mv [파일/폴더명] [위치]` : 파일 또는 폴더 이동