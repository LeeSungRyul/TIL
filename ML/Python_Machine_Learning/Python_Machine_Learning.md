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
  - `L(y, ^y) = (y - ^y) ** 2`

- 변경된 w와 b에 대한 Loss 비교

  - Cost(Mean Squared Error)는 Loss들의 평균

  - Cost(y, ^y) = mean(L(y, ^y)) = mean((y - ^y) ** 2) = mean((y - (wx-b)) ** 2)

  - w = w - r(Hyperparameter: Learning Rate. Step size) * dw(경사값)

    b = b - r * db



## 3. Model Validation

- Validation : 사용에 적합한가 확인

- `Model Capacity` : parameter의 개수

- `Training Error` : Training Data에 Model을 적용하여 확인한 실제값과 예측값의 차이(오차)

  - 최적의 Model 선택. 하지만 Model 생성과 평가에 같은 데이터를 사용하여 부작용 발생(Overfitting)
  - mean((y - y_hat) ** 2)

- `Overfitting` : 학습된 결과가 트레이닝 데이터**에만** 최적화된 모델

  - 모델 생성 시 활용하지 않은 데이터에는 성능이 급격하게 낮아짐

- Generalization Error

- Testing Error : 모델은 **학습(모델 생성)** 후 반드시 **평가(모델 평가)** 필요

  - Training Data(for **학습**) / Testing Data(for **평가**)

- Model Validation(p. 76) 

  - ML/DL 모델링의 목적 : 일반화된 Model 을 만드는(학습시키는) 것

    -> Model 생성(학습) 시 사용되지 않은 Data에서도 유사한 성능을 제공

    (Training Error와 Test Error의 차이가 크지 않도록, 즉 Overfitting 되지 않는 Model)

  - Validation Approach : 데이터셋을 3개로 나눔. 미래의 오차가 어느정도일지 추정
    - Training Error : 트레이닝 데이터로 모델들을 만듦
    - Validation Error : 최적화된 모델을 선정
    - Testing Error : 일반화 에러를 추청
  
- Regularization(규제화. 정규화) : Model이 Train Data에 너무 학습되지 않도록 방해하는 것

  - mean((y - y_hat) ** 2) + a * 시그마(wi)**2 (a : 0(규제 없음) ~ 1(규제 강함))

    ​										+ a * 시그마|wi|




## 4. Regression Analysis. 수치 예측

- 회귀모델 : `y(연속형 데이터. 종속변수. 반응변수) ~ wx(독립변수. 설명변수) + b` 사용하여 w, b 값 추정

- 과거의 결과값(데이터)를 기준으로 미래의 결과값(수치)를 **예측**하는 방법

  -> 미래에 발생할 결과값이 "과거의 평균으로 돌아간다(회귀)"

- 상관계수(-1 <= r <= 1)

- Scaling p. 177

  - 범위가 다른 변수들의 범위를 비슷하게 맞추기 위한 목적 (단, 분포(모양)은 변경되면 안 됨)

  - 연속형 변수가 다양한 범위로 존재하면 제곱 오차 계산 시 왜곡 발생

  - Normalization(정규화) : 변수의 스케일을 0 ~ 1 사이 범위로 맞추는 것

    X_nomalization = (X - min(X)) / (max(X) - min(X))

  - Standardization(표준화) : 변수의 평균을 0, 표준편차를 1로 만들어 표준정규분포의 특징을 갖도록 함

    X_standardization = (X - mean(X)) / std(X)

- - 단일회귀분석 : Output(y)에 영향을 주는 Input(x)이 1개
  - 다중회귀분석 : Output(y)에 영향을 주는 Input(x)이 여러개

- Encoding

  - Integer Encoding : 문자형 변수를 숫자형 변수로 변경하여 변수 연산 범위를 확대
  - One-Hot Encoding : 하나의 값만 True(1)이고 나머지 값은 False(0)인 인코딩



## 5. Logistic Regression. 범주 예측

- Classification(분류) 모델 : Output(y)의 수치예측이 아닌 어떤 범주에 속하는지에 대한 예측(확률)을 모델링

  - 종류 : Binary(이진) / Categorical(다중)
  - Regression(수치예측) 모델에 Sigmoid() 필터 적용하여 구현

- y = sigmoid(wx  + b)

  - sigmoid(x) = 1 / (1 + e ** (-x))
  - 일반적으로 분류 기준을 0.5로 지정. 0.5보다 크면 1, 작으면 0으로 분류
  - w : 기울기 / b : 좌우이동 -> 학습 : Gradient Descent

- 분류 결과에 대한 추가적인 신뢰도 검증 필요(Model Validation) p.356 -> Confusion Matrix

  - Binary Confusion Matrix(더 알고 싶은 정보를 Positive)

    |         |          |  분류결과(y_hat)   |                    |
    | :-----: | :------: | :----------------: | :----------------: |
    |         |          |      Positive      |      Negative      |
    | 실제(y) | Positive | True Positive(TP)  | False Negative(FN) |
    |         | Negative | False Positive(FP) | True Negative(TN)  |

    - 정확도(Accuracy) : 맞게 분류된 비율. (TP + TN) / (TP + TN + FP + FN)
    - 정밀도(Precision) : Positive 분류 결과 중 실제 Positive 비율. TP / (TP + FP)
    - 재현율(Recall) : 실제 Positive 중 Positive로 분류된 비율. TP / (TP + FN)
    - Precision 과 Recall은 Trade-Off 관계
    - F1-Score : Precision과 Recall의 조화평균. 0~1
    - Business Impact : 어떤 일에 부정적인 영향을 주는 정도

- Cross Entropy Error

  - 서로 다른 사건의 확률을 곱하여 Entropy 계산

  - Binary CEE = -y * log(y_hat) - (1 - y) * log(1 - y_hat)

  - Information Theory(정보 이론)

    - Information Gain(정보 이득량) : **자주 발생하지 않는 사건**은 자주 발생하는 사건보다 전달하는 **정보량**이 많음

      정보 이득량은 정보의 희귀성(발생 가능성)에 반비례

      I(x) = -log(P(x))

    - Degree of Surprise : 예상하기 어려운 정보에 더 높은 가치를 매기는 것

  - Entropy(불순도) : 확률변수의 평균 정보량(기대값)

    - 놀람의 평균 정도
    - Entropy = E(-log(P(x)))
    - -sum(p(x) * log(p(x)))
    - Entropy가 낮으면 분류 정확도가 높아짐



## 6. Decision Tree p.101

- Machine : Function(y = wx + b) / Tree(Rule)
- 가능한 대답이 두가지인 이진 질의(Binary Question)의 분류 규칙을 바탕으로 최상위 루트 노드(Root Node)의 **질의 결과(Rule)**에 따라 브랜치(Branch)를 차고 이동하고 최종적으로 분류 또는 예측값을 나타내는 리프(Leaf)까지 도달
  - 범주형 자료 : Classification Tree(분류 트리)
  - 수치형 자료 : Regression Tree(예측 트리)
- Root Node : 최상위 노드
  - Splitting : 하위 노드로 분리되는 것
  - Branch : 노드들의 연결
- Decision Node : 2개의 하위 노드로 분리되는 노드
  - Parent Node : 분리가 발생하는 노드
- Leaf(Terminal Node) : 더이상 분리되지 않는 최하위 노드
  - Children Node : 분리가 발생한 후 하위 노드
- 분리 과정을 반복하면서 Decision Tree가 성장 -> Model Capacity가 커지면서 Overfitting 가능성도 커짐
- 과적합(Overfitting) 문제 : 각 노드는 동질성이 높고 불순도가 낮은 방향으로 분리
  - 너무 복잡하고 큰 의사결정나무 모델을 생성하여 과적합 문제 발생
- 대응방법 - 가지치기(Pruning)
  - 모델 성능 향상 및 과적합 예방 목적
  - HyperParameter
    - max_depth : 의사결정나무의 성장 깊이
    - min_samples_leaf : 리프에 들어가는 최소 샘플의 개수
- Entropy vs. Gini Impurity Index
  - Entropy
    - 분리 정보 이득이 큰 특징으로 분리 발생
    - 분리 정보 이득 = 질문 전 Entropy - 질문 후 Entropy



## 7. Random Forest(Ensemble) p.115

- Regression : 선형모델 / 나무모델 / 신경망

- **덜 정확한 분류모델** 여러 개를 모아서 더 정확한 분류모델을 만들 수 있을지?

  - 앙상블(Ensemble) : 여러가지 모델 사용하여 정확도를 개선하는 방법

- 랜덤 포레스트 : 의사결정나무의 앙상블

  - 다수의 의사결정나무의 결과로부터 모델을 생성

  - 모델 생성에 **다양성(Diversity)**과 **임의성(Random)** 부여
  - 모델 정확도 높이고, 과적합 발생 가능성 낮춤
  - 올바른 예측은 강화하고, 잘못된 예측은 상쇄하는 경향 존재

- 다양성(Diversity)

  - 배깅(Bagging) : Bootstrap + Aggregating
    - 주어진 데이터를 사용하여 여러 개의 서로 다른 Train Data 생성
    - 생성된 Train Data마다 별도의 의사결정나무 모델 생성
    - Hyperparameter(n_estimators)로 의사결정나무 개수 지정
  - Train Data는 Bootstrap 방식으로 생석
    - Bootstrap Data는 Original Data에서 단순 복원 임의추출법(같은 값 중복 가능)으로 생성
  - Aggregating : 여러 개의 Bootstrap 모델의 결과를 통합
    - 분류 모델 : 다수결 또는 가중치를 적용하여 통합
    - 예측 모델 : 평균값 또는 가중평균값으로 통합

- 임의성(Random)

  - 의사결정나무 생성 시 변수 무작위 선택
  - 무작위 입력 변수의 개수를 1~전체 변수의 개수 사이에서 지정
  - Hyperparameter : max_features(기본값 : sqrt(변수의 개수))

- Hyperparameter Tuning

  - **n_estimators** : 모델에 사용되는 의사결정나무 개수
  - **max_features** : 분할에 사용되는 Feature의 개수
  - **max_depth** : 트리 모델의 최대 깊이 지정
  - max_leaf_nodes : 말단 노드의 최대 개수
  - min_samples_split : 분할을 위한 최소한의 샘플데이터 개수
  - min_samples_leaf : 말단노드가 되기 위한 최소한의 샘플 데이터 개수

- Cross Validation(교차 검증) : Overfitting 방지하기 위해 수행

  - Validation을 한번만 수행하면 특정 Data에만 최적화될 수 있음
  - 다양하게 Training Data와 Validation Data를 변경하면서 모델 평가

- K-Fold Cross Validation : Training Data를 무작위로 균등하게 K개의 그룹으로 나눠서 검증

  - (K-1)개의 Training Fold와 1개의 Valifation Fold 지정
  - K는 Hyperparameter. 일반적으로 5~10 정도로 선택
  - K개의 결과의 평균을 Validation Data에 적용하여 평가



## 8. K-means Clustering p.225

- 비지도 학습(입력값에 대한 출력값이 정해져 있지 않음). 가상의 중심점을 각 군집 내 평균점으로 이동하면서 반복
- 데이터 간 유사성을 계산하여 유사성이 높은 개체의 군집 생성
- 동일 그룹 내 데이터는 유사성 높고, 그룹 간에는 유사성 낮음
- 각 군집 내 데이터 간 거리를 최소화. 각 군집 간 거리를 최대화
- 최초 K개의 의사 중심점 지정
- 몇 개의 군집으로 분류? 주관적으로 비지니스 의사결정에 도움 주는 수. 군집 개수 늘리면 데이터간 유사성 증가, 인접 군집과 차이점 감소
- 주성분 분석(PCA)
  - 데이터 포인트를 가장 잘 구별해주는 배후의 변수(주성분)을 찾는 기법
  - 주성분(적은 수의 변수)으로 데이터셋을 표현 가능(차원 축소 기법)
  - 주성분은 데이터 포인트가 가장 넓게 분포(분산이 큰)하는 차원을 의미
  - 주성분 분석의 목적 변수는 "새로운 변수"

## 9. Association Rules

- 비지도 학습. 데이터 포인트 사이의 연관 규칙을 찾는 방법
- 연관 규칙 : 특정 사건 발생 시 함께 자주 발생(조건부 확률)하는 다른 사건의 규칙
- 지지도(Support) : 특정 품목 집합이 얼마나 자주 등장하는지. 특정 품목 집합을 포함하는 거래 비율로 계산. 방향성 없음
  - Support = A와 B가 동시에 포함된 거래수 / 전체 거래수
  - 지지도 임계값(Support Threshold) : 빈번한 품목 집합을 구분하는 기준 -> 임계값보다 지지도가 큰 품목은 빈번히 등장하는 것으로 볼 수 있음
- 신뢰도(Confidence)
  - (상품A)->(상품B) : 상품A(조건)가 존재할 때 상품B(결과)가 나타나는 빈도
  - A와 B가 동시에 포함된 거래수 / A를 포함한 거래수 = Support(A,B) / Support(A)
- 향상도(Lift) : 두 물품이 각각 얼마나 자주 거래되는지 고려. A와 B가 함께 팔리는 빈도
  - 향상도가 1보다 크면 A 거래 시 B도 함께 거래될 가능성 있음
  - 향상도가 1보다 작으면 A 거래 시 B도 함께 거래될 가능성 작음
  - 향상도 = 1 : 독립사건
  - Lift = Confidence(A->B) / Support(B)



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