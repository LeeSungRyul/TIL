## ✅2차원 리스트 ➡ 1차원 리스트

- sum 함수 사용

  ```python
  my_list = [[1, 2], [3, 4], [5, 6]] print (sum(my_list, []))
  ```

- itertools.chain 사용

  ```python
  import itertools my_list = [[1, 2], [3, 4], [5, 6]] print(list(itertools.chain.from_iterable(my_list)))
  print (list(itertools.chain(*my_list)))
  ```

- list comprehension 사용

  ```python
  my_list = [[1, 2], [3, 4], [5, 6]] 
  print ([element for array in my_list for element in array])
  ```

- functools.reduce 사용

  ```python
  from functools import reduce 
  import operator 
  
  my_list = [[1, 2], [3, 4], [5, 6]] 
  print (list(reduce(operator.add, my_list)))
  print (list(reduce(lambda x, y: x+y, my_list)))
  ```

  - my_list의 각 원소를 operator.add라는 덧셈 연산자 통해 새로운 리스트에 각 원소를 추가

- numpy flatten 사용

  ```python
  import numpy as np my_list = [[1, 2], [3, 4], [5, 6]] print (np.array(my_list).flatten().tolist())
  ```

- 시간: numpy < from_iterable = itertools_chain = comprehension < sum

