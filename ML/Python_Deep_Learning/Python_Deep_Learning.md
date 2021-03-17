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

    - Perceptron: y = w1 * x1 + w2 * x2 + b

      - w1 = w1 - step * dw1
      - w2 = w2 - step * dw2
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