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

## ✅직사각형

```python
T = 4

for tc in range(T):
    sq1_xmin, sq1_ymin, sq1_xmax, sq1_ymax, sq2_xmin, sq2_ymin, sq2_xmax, sq2_ymax = map(
        int, input().split()
    )

    if sq1_xmax < sq2_xmin or sq2_xmax < sq1_xmin or sq1_ymax < sq2_ymin or sq2_ymax < sq1_ymin:
        ans = "d"
    elif (
        (sq1_xmax == sq2_xmin and sq1_ymax == sq2_ymin)
        or (sq1_xmin == sq2_xmax and sq1_ymax == sq2_ymin)
        or (sq2_xmax == sq1_xmin and sq2_ymax == sq1_ymin)
        or (sq2_xmin == sq1_xmax and sq2_ymax == sq1_ymin)
    ):
        ans = "c"
    elif (
        (sq1_ymin == sq2_ymax and (sq1_xmin < sq2_xmin or sq2_xmin < sq1_xmax))
        or (sq1_ymin == sq2_ymax and (sq1_xmin < sq2_xmax or sq2_xmax < sq1_xmax))
        or (sq1_xmax == sq2_xmin and (sq1_ymin < sq2_ymin or sq2_ymin < sq1_ymax))
        or (sq1_xmax == sq2_xmin and (sq1_ymin < sq2_ymax or sq2_ymax < sq1_ymax))
        or (sq2_ymin == sq1_ymax and (sq2_xmin < sq1_xmin or sq1_xmin < sq2_xmax))
        or (sq2_ymin == sq1_ymax and (sq2_xmin < sq1_xmax or sq1_xmax < sq2_xmax))
        or (sq2_xmax == sq1_xmin and (sq2_ymin < sq1_ymin or sq1_ymin < sq2_ymax))
        or (sq2_xmax == sq1_xmin and (sq2_ymin < sq1_ymax or sq1_ymax < sq2_ymax))
    ):
        ans = "b"
    else:
        ans = "a"

    print(ans)
```

- 조건이 많아서 까다로운 문제...
- 가장 제외하기 쉬운 겹치지 않는 조건부터 시작하여 가장 고려해야 할 것이 많은 조건을 else로 처리
- "b"에서 겹치지 않는 부분은 "d"에서 처리되므로, `(sq1_xmin < sq2_xmin or sq2_xmin < sq1_xmax)`와 같이 or로 처리해야 정답 처리

