<교재>

1. 메인 교재 : '**파이썬 라이브러리를 활용한 머신러닝**' (중 `sklearn` 위주)

2. '모두의 데이터분석' : 많이 참고하지 않음

3. '데이터 과학을 위한 통계' : 교재 중 실습 예제는 R 사용

 

------

# **Python Data Analytics**

## Data Analytics란?

### Data의 특징

1. 생성(만들어진다) 
2. Activity(행동)의 결과 (Business Activities)
3. 여러개
4. 과거

`즉, '데이터'는 과거 행동의 결과들`

### Data Analytics

데이터(과거 행동의 결과들)의 특징을 확인하는 일. 이를 통해 미래 행동의 결과를 예측.

### Statistics(통계)

- 평균 : 중심화 경향치
- 분산 : 산포도. 평균에서 평균적으로 떨어져 있는 정도
- 표준편차 : 분산의 루트값
- 데이터에 따라 연산의 적용 가부가 달라짐



## Data Structure

- 데이터를 모아서 관리하는 방식
- Python(String, List, Tuple(정형) / Dictionary(비정형))  VS  Analytics(Pandas: Data Frame - Table(RDB))

### Data -> Computer(0, 1)

- bit(Binary Digit)

### Address / Index

- Memory(물리적 공간)에 부여한 Address(논리적인) 구조



## 정형/구조화/Structured 데이터

- 입력 데이터 크기가 정해진 데이터
- Statistics(통계) 또는 ML(Machine Learning)로 처리 / 비정형 데이터는 DL(Deep Learning)
- NoSQL : 비정형 데이터 관리





# 개발 환경

## Google Colab

- 설치 필요 없는 클라우드 기반의 무료 Jupyter Notebook 환경

- 크롬 브라우저 환경을 통해 코드를 작성, 실행하여 분석 수행

- GPU 및 TPU 컴퓨팅 환경 지원

- Colab에서 작성된 스크립트는 Google Drive에 자동 저장(Colab Notebooks DIR)
  - 파일 열 때는 구글 드라이브에서 파일 오른쪽 클릭 하면 연결 앱에서 Google Colaboratory
  - 구글 드라이브 설정에서 Google Colaboratory 기본 앱으로 설정하면 더블 클릭으로 실행 가능



## 사용법

- 코드 실행 : ctrl + Enter / shift + Enter / alt + Enter(아래 실행 줄 새로 생김) / 코드 좌측 실행이미지 클릭
- `+텍스트` : 주석 삽입. html, md와 문법 동일
- `수정-모든 출력 지우기` : 실행 결과 모두 삭제
- 사용자 모듈 : 좌측 메뉴 중 파일에 모듈 파일 삽입