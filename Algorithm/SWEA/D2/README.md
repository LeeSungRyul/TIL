## ✅1859

- 첫 접근 - 재귀함수

``` python
def calc_profit(lst):
    max_idx = lst.index(max(lst))

    if max_idx != len(lst) - 1:
        return (max(lst) * max_idx - sum(lst[:max_idx])) + calc_profit(lst[max_idx + 1:])
    else:
        return max(lst) * max_idx - sum(lst[:max_idx])
```

- 두 번째 접근 - 반복문(앞에서부터)

```python
def calc_profit(lst):
    ans = 0
    start = 0

    while True:
        max_idx = lst.index(max(lst[start:]))
        ans += max(lst[start:]) * (max_idx - start) - sum(lst[start:max_idx])
        start = max_idx + 1
        
        if start >= len(lst) - 1:
            break
    return ans
```

- 최종

```python
def calc_profit(lst):
    ans = 0
    max_price = lst[-1]

    for i in range(len(lst) - 2, -1, -1):
        if max_price < lst[i]:
            max_price = lst[i]
        else:
            ans += max_price - lst[i]
    return ans
```

- 정리

  재귀함수의 경우 메모리 초과.

  반복문의 경우, 반복문 안에서 list 값들을 탐색하는데 탐색 과정에서 시간 소요되어 시간 초과나는 것으로 보임.

  다른 풀이 참조하여, 뒤에서부터 접근하여 가장 마지막 값을 max 값으로 두고 max 값보다 큰 경우 max 값 갱신하고, 아닌 경우 max 값에서 해당 값 빼준 값을 더해줌