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
  - y = w*X + b
- Multi_Layer Perceptron
  - 