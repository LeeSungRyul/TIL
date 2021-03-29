# 1. Multi-Layer Perceptron(ANN)

- 지도 학습

## 1) Neural Network

- ANN(Artificial Neural Network)
  - 수치예측, 범주예측, 패턴인식, 제어분야에 응용
  - 인간의 뇌 구조를 모방하여 만들어짐
  
- Perceptron
  - 인공신경망의 한 종류(선형 분리기)
  - 가장 간단한 형태의 Forward Network
  - 동작원리 : 노드의 입력값과 가중치의 곱을 모두 합
    - 합한 값이 활성화 함수의 임계치보다 크면 1, 작으면 0을 출력
  - y = W*X + b
  
- Multi-Layer Perceptron(MLP)

  - 다층 퍼셉트론: 퍼셉트론으로 해결할 수 없는 **비선형 분리 문제**에 필요

  - 여러 층의 퍼셉트론을 쌓아서 동작(Input - Hidden - Output)

  - Deep Neural Network(DNN): Hidden layer가 여러 개

  - Parameter 학습법: Gradient Descent

    - 경사하강법 사용하여 W와 b를 학습

    - Perceptron: y = W1 * X1 + W2 * X2 + b

      - W1 = W1 - step * dW1
      - W2 = W2 - step * dW2
      - b = b - step * db

    - Tensor: Multi Dimensional Matrix

      ```python
      def Machine(x1, x2,
                w1_11, w1_12, b1_1,
                w1_21, w1_22, b1_2,
                w2_11, w2_12, b2_1):
          y1 = sigmoid(x1*w1_11 + x2*w1_12 + b1_1)
          y2 = sigmoid(x1*w1_21 + x2*w1_22 + b1_2)
          y_hat = sigmoid(y1*w2_11 + y2*w2_12 + b2_1)
      	
          return y_hat
      
      ```

- softmax()

  - 출력층에서 다중 분류 수행
    - softmax() 함수의 출력값 범위: 0 ~ 1(확률값)
  - sigmoid() vs. softmax()
    - sigmoid(): 함수 출력값이 각각 0 ~ 1사이의 값 가짐
    - softmax(): 전체 출력값의 합이 1이 되어야 하므로 학습효과 증가

- Categorical Classification

  - Categorical Cross-Entropy Error(CEE)
  - MSE vs. CEE
    - y1 = [1, 0, 0], **y2 = [0, 1, 0]**,  y3 = [0, 0, 1]
    - y_hat = [0.1, 0.7, 0.2]
    - MSE = ((0 - 0.1)^2 + (1 - 0.7)^2 + (0 - 0.2)^2) / 3
    - CEE = -0 * log(0.1) - 1 * log(0.7) - 0 * log(0.2)

# 2. Error Backpropagation

- Forward Propagation

  - 각 학습단계의 Parameter Update 위해 Parameter 별 **편미분값** 필요
  - w = w - r * **dw**
  - Parameter 개수 증가는 학습 시간에 부정적 영향

- Chain Rule: 노드(Function)들의 연결 -> 합성(중첩) 함수

  - Multi-Layer Perceptron의 구조적 한계점 극복
  - 미분의 연쇄 법칙(Chain Rule)을 반복적으로 적용하는 알고리즘
    - Neural Network는 **간단한 함수들의 중첩**(합성 함수)으로 구성
    - 합성 함수 미분은 합성 함수를 구성하는 **개별 함수 미분의 곱**으로 처리
  - y_hat = sigmoid(W3 * sigmoid(W2 * sigmoid(W1*X + b1) + b2) + b3)
    - Input(X) -> f1() -> f2() -> f3() -> Output(y_hat)

- Backpropagation Algorithm: 수치미분과정 없이 미분값을 획득. Keras 교재 p.86

  - Forward propagation 수행하여 y_hat 계산
    - y와 y_hat 사용하여 오차값 계산

  - 학습: 오차값이 감소하는 방향으로 weight 수정
    - 효율적인 경사값(Gradient) 계산 위해 Backpropagation 수행
    - Parameter Update 위해 출력층의 오차값을 은닉층으로 전달
  - 미분의 연쇄 법칙 + 오차 역전파 알고리즘
    - 수치미분 과정 없이 학습 위한 경사값 계산
    - Hidden Layer나 Node 증가해도 빠른 속도로 학습 가능

- Vanishing(0이 된다) Gradient(학습을 위한 미분값)

  - 역전파는 출력층으로부터 하나씩 앞으로 돌아오면서 각 층의 가중치를 학습
    - 신경망 모델의 가중치 학습에 미분값, 즉 기울기 필요
    - Sigmoid 함수를 미분하면 최대치가 0.25로 1보다 작은 값 생성
    - 은닉층이 증가하면 미분값(기울기)이 0이 되는 문제 발생
    - 대응책: Activation Function(Sigmoid)을 다른 함수로 대체하여 학습

# 3. Optimization Method



# 4. Keras TensorFlow

- TensorFlow
  - 데이터 흐름 프로그래밍을 위한 Open Source SW Library
  - 플랫폼 관계 없이 모델 학습시키고 배포 가능
  - 빠른 프로토타입 제작과 디버깅 구현 가능
- Keras
  - Python 기반의 Deep Learning Framework(Library)
  - 내부적으로는 TensorFlow, Theano, CNTK 등 Deep Learning 전용 엔진 구동
  - 다중 입력 및 다중 출력 구성 가능
  - 사용자 중심의 상위 레벨 인터페이스 제공
    - 하위 레벨 계산은 일반적으로 TensorFlow 사용
    - 동일한 코드를 CPU 및 다양한 GPU에서 실행 가능
- Keras with GPU
  - CPU: 복잡한 연산 수행에 적합
  - GPU: 단순한 대량 연산에 적합
    - Deep Learning Matrix 연산에 활용
- Tensor: 다차원 행렬
  - Neural Network 학습의 기본 데이터 단위
    - **숫자(Numeric. 실수)** 데이터를 담기 위한 컨테이너
    - 임의의 차원(Dimension) 또는 축(Rank)을 가짐
  - Tensor in NLP(Natural Language Processing)
    - 문장과 단어를 숫자 벡터로 매핑
  - Tensor in Grayscale Image(흑백 이미지)
    - (Number of Images, Rows, Columns) : Rank 3 Tensor
  - Tensor in RGB Color Image
    - (Number of Images, Rows, Columns, RGB Channel) : Rank 4 Tensor
  - Tensor in RGB Color Video
    - (Video Frames, Number of Images, Rows, Columns, RGB Channel) : Rank 5 Tensor

- Keras Modeling
  - Define(모델 신경망 구조 정의): Sequential Model, Layers/Units, Input_shape, Activation
  - Compile(모델 학습방법 설정): Loss, Optimizer, Metrics
  - Fit(모델 학습 수행) -> Parameter Update: Train Data, Epochs, Batch Size, Validation Data
  - Evaluate(모델 평가): Plot, Evaluate
  - Predict(모델 적용): Probability, Classes

# Deep Neural Network

- Keras Modeling



# Convolutional Neural Network

- 합성곱(Convolutional) 신경망 알고리즘
  - 이미지 처리 작업에 주로 사용
  - 합성곱 연산을 이용하여 **가중치의 수를 줄이고** 연산량 감소
  - 여러 개의 Filter(Parameter Matrix)로 이미지의 특징(Feature Matrix)를 추출
  - Hyperparameter
    - Filter: Filter를 Input_Data에 적용하여 특징 맵(Feature Map) 생성
      - Filter 값은 Input_Data의 특징을 학습하는 가중치 행렬
      - 동일한 Filter로 Input_Data 전체에 합성곱 연산 적용
    - Stride: Filter 적용 위해 이동하는 위치의 간격
    - Pooling: 가로 및 세로 방향으로 크기를 줄이는 연산. 이미지의 커다란 특징만 뽑아내는 것
      - Pooling Window 및 Stride 값 지정
      - Max Pooling / Average Pooling
    - Padding
- ImageNet Moment
  - 전이학습(Transfer Learning): 사전 학습된 Parameter(Model)을 가져와서 적용
    - Input shapeDNN Layer 재활용 불가
  - ImageNet: 100만 장이 넘는 이미지를 담고 있는 데이터셋
  - ILSVC(ImageNet Large Scale Visual Challenge): 1000가지의 이미지 클래스를 분류하는 문제
  - Fine Tuning
  - Image Processing

# Recurrent Neural Network(순환 신경망)

- Feed-Forward Neural Network와의 차이점
  - 전 단계의 기억(Short-Term Memoty)을 가지고 동작
- DNN과 CNN 신경망
  - 각 Layer 간 상태를 기억하지 않고 입력과 출력이 독립적으로 처리
  - **각 Layer마다 독립적**으로 가중치(Weight)를 학습
- 순환 신경망 - 내부 루프가 존재하는 신경망
  - 은닉층의 출력이 계속 순환하면서 입력값과 함께 학습에 사용
  - 연속적 데이터 처리를 위해서는 이전 단계의 정보 필요
  - 학습 단계에서 **모든 Layer가 같은** 가중치(Weight)를 공유
  - one to one: 이미지 분류
  - one to many: 이미지 설명 문장
  - many yo one: 여러 개의 입력에 대한 감정 분석
  - many to many: 기계번역
- RNN
  - 순차적인 정보를 처리하기 위한 모델
    - 앞뒤 순서(상호관계)가 존재하는 시계열 데이터
    - 텍스트나 음성 데이터 처리(번역, 음성인식, 음악, 동영상)
- ht <- tanh(Wx * Xt + **Wh * ht-1** + b)
  - Single Layer가 반복
- 

