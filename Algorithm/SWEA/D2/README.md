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

## ✅2005

```python
T = int(input())

def triangle(num):
    ans = [[1]]

    if num == 1:
        return ans

    for i in range(1, num):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(temp)
    return ans

    return ans

for i in range(T):
    N = int(input())

    ans = triangle(N)

    print(f'#{i+1}')
    for line in ans:
        print(' '.join(map(str, line)))
```

- 의문

  try/except 구문으로 IndexError일 때 예외처리 해보려 했으나, 첫 번째 인자의 경우 -1이 오류에 해당하지 않아 불가

  for문을 2개 쓰지 않고 해결하는 방법은 없을까?

## ✅2005, 2001

- 2중, 3중 for문 중첩 말고 다른 풀이는 없을까?



## ✅1979

```python
T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    total_map = []
    for j in range(N):
        total_map.append(list(map(int, input().split())))

    ans = 0
    # 가로 방향
    for k in range(N):
        cnt = 0
        for l in range(N):
            if total_map[k][l] == 1:
                cnt += 1
            if total_map[k][l] == 0 or l == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0
    # 세로 방향
    for l in range(N):
        cnt = 0
        for k in range(N):
            if total_map[k][l] == 1:
                cnt += 1
            if total_map[k][l] == 0 or k == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{i} {ans}')
```

- 문제점

  N 범위를 초과했을 때 `cnt` 체크하도록 `if total_map[k][l] == 0 or k == N` 과 같은 방식으로 접근하였더니 메모리 에러

- 핵심

  1인 구간을 만날 때 `cnt` 값 1씩 더함. 0인 구간을 만났는지 혹은 끝에 도달했는지 `if` 문으로 하고 `else`에서 더하려고 하면 안 됨. 먼저 1인지 체크하고 그 다음 벽이나 끝인지 여부 판단

