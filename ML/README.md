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

**데이터(과거 행동의 결과들)의 특징**을 확인하는 일. 이를 통해 미래 행동의 결과를 예측.

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



## 결측치 처리

1. 삭제(제거) : 행 / 열 -> 올바른 특징 확인인지 문제
2. 대체 : 수치(평균 등) / 문자(최빈값 등)





# 파이썬 라이브러리를 활용한 머신러닝

## 1. AI(Artificial Intelligence)

- 인공장치들의 지능을 설계하는 것. 인공장치가 인간의 지능을 모방하는 것
  - 지능(Intelligence) : 인간이 행하는 지적 작업의 주체
- AI Type
  - 약한 인공지능(ANI: Artificial Narrow Intelligence) : 많은 데이터 처리하여 **특정 기능**만 수행
  - 강한 인공지능(AGI: Artificial General Intelligence) : 사람처럼 생각하고 판단하는 **범용** 인공지능
- 튜링 테스트 : 컴퓨터가 지능을 가지고 있는지 여부를 조사. 인간과 컴퓨터에게 같은 질문을 하여 구분할 수 없으면 컴퓨터가 지능을 갖고 있는 것으로 간주

## 2. ML(Machine Learing) (*Gradient Descent*)

- 학습 : y = ax + b에서 a, b(parameter)를 주어진 데이터에 맞춰 변화(최적화)시키는 것

  학습이란 "어떤 **작업**에 대해 특정 기준으로 측정한 성능이 새로운 **경험**으로 인해 **향상**되었다면, 그 프로그램은 어떤 **작업**에 대해 특정 기준의 관점에서 새로운 **경험**으로부터 **'배웠다'**라고 말할 수 있다."

  -> Learning : 학습 이후 새로운 데이터에 대해 학습된 내용으로 처리하는 것

- ML : 머신이 **코드로 명시되지 않은 동작**을  **데이터로부터 학습**하여 **실행**할 수 있도록 하는 알고리즘

  - 데이터로부터 **일관된 패턴** 또는 새로운 지식을 찾아내(학습하)는 방법
  - **학습된 알고리즘(Model)**을 적용하여 정해진 업무를 처리
  - 학습할 수 있는 것과 **학습할 수 없는 것**을 구분하는 것이 중요

### Gradient Descent(경사 하강)

- ML 학습의 원리

- Function : y = **w**x + **b** (**w**eight: 가중치, **b**ias: 편향)

- Loss Func for Regression Analysis

  - y : 실제값(연속형 데이터)	^y : 예측값
  - Loss Func : 실제값과 예측값의 차이(Error/Loss/Cost : 오차)를 비교하는 지표
  - L(y, ^y) = (y - ^y) ** 2

- 변경된 w와 b에 대한 Loss 비교

  - Cost(Mean Squared Error)는 Loss들의 평균

  - Cost(y, ^y) = mean(L(y, ^y)) = mean((y - ^y) ** 2) = mean((y - (wx-b)) ** 2)

  - w = w - r(Hyperparameter: Learning Rate. Step size) * dw(경사값)

    b = b - r * db



## 3. Model Validation

- Validation : 사용에 적합한가 확인

- Model Capacity
- 



## 4. Regression Analysis. 수치 예측

## 5. Logistic Regression. 범주 예측

## 6. Decision Tree

## 7. Random Forest(Ensemble)

## 8. K-means Clustering

## 9. Association Rules





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
- github 파일 링크 사용 : github 파일의 Raw의 링크