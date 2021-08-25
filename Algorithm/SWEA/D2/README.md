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

## ✅1928_Base64Decoder

### 1. 내 풀이

```python
T = int(input())

for tc in range(1, T+1):
    test_case = input()
    
    binary_str = ''
    for char in test_case:
        if 'A' <= char <= 'Z':
            num = ord(char) - 65
        elif 'a' <= char <= 'z':
            num = ord(char) - 71
        elif '0' <= char <= '9':
            num = ord(char) + 4
        elif char == '+':
            num = ord(char) + 19
        elif char == '/':
            num = ord(char) + 16
        
        binary_char = bin(num)[2:].zfill(6)
        binary_str += binary_char

    ans = ''
    for j in range(0, len(binary_str)-7, 8):
        ans += chr(int(binary_str[j:j+8], 2))

    print(f'#{tc} {ans}')
```

- 배운 점

  문자열의 `.zfill(width)` 메서드 활용하면 width의 길이보다 문자열이 짧을 경우, 왼쪽의 공백을 0으로 채워줌

  비슷한 메서드로는 `.rjust(width[, fillchar])`로 fillchar 따로 설정 가능

  반대로 오른쪽 공백에 원하는 문자 채우려면 `.ljust(width[, fillchar])`

  `.center(width[, fillchar])`는 가운데 정렬하며 좌우 빈 공간 fillchar로 채우고 좌우 공백 다를 경우 오른쪽 공백에 하나 더 할당

  `bin()` 함수의 return 값은 '0bxxx' 형태의 문자열

  `int(num, 2)`로 2진수 다시 10진수로 변환할 때 `num`은 문자열로 '0b' 붙이지 않아도 변환 가능

### 2. 구글링 통한 다른 사람 풀이

```python
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
```

- `list`에 인코딩 문자를 넣어 index로 접근하면 하나씩 ord로 바꿔주지 않아도 됨

### 3. b64decode

```python
from base64 import b64decode
 
T = int(input())
 
for tc in range(1, T + 1):
    word = input()
    res = b64decode(word).decode('UTF-8')
 
    print(f'#{tc} {res}')
```

## ✅4881

```python
from itertools import permutations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N  # 각 숫자가 10 미만 자연수이므로 무조건 10*N보다 작음
    for_permutation = list(range(N))

    for permutation in permutations(for_permutation, N):
        temp = 0
        for i in range(N):
            temp += data[i][permutation[i]]
            if temp >= ans:
                break
        if temp < ans:
            ans = temp

    print("#{} {}".format(tc, ans))
```

- 직접 모든 순열을 만들고 해당 순열의 합을 구할 때, 계속 시간 초과가 나서 내장된 `permutaions()`를 사용하여 중간에 `temp`가 `ans`보다 커지면 `break`해주는 식으로 했더니 일단 통과

```python
T = int(input())

def permutation(idx, total):
    global ans  # idx == N 되어 해당 순열의 합 계산할 때, ans보다 작으면 갱신해줘야 하므로 global 활용

    if idx == N:  # 순열 완성
        if total < ans:
            ans = total
        return

    if total >= ans:
        return

    for i in range(N):
        if check[i] == 0:
            sel[idx] = i
            check[i] = 1
            # total += data[idx][sel[idx]] 함수에서 더하면 아래서 빼주지 않아도 됨
            permutation(idx + 1, total + data[idx][sel[idx]])
            # total -= data[idx][sel[idx]]
            check[i] = 0

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N  # 각 숫자가 10 미만 자연수이므로 무조건 10*N보다 작음

    sel = [0] * N  # 순열을 만들어줄 리스트. sel[idx]는 data[idx]의 column 인덱스
    check = [0] * N  # 현재 순열에 들어가있는 숫자 체크 위한 리스트

    permutation(0, 0)

    print("#{} {}".format(tc, ans))
```

- `sel`은 순열을 만들어줄 list이고, `check`는 해당 column을 사용했는지 여부 체크
- `permutation`함수 내에서 `total` 계산해주면 위아래에서 더하고 빼줄 필요 없음
- `sel`에는 0 ~ N-1 까지의 column 인덱스가 들어가야 하므로, for문에서 i를 입력받은 idx에 넣어주고, total에는 idx row의 sel[idx]의 값을 column 인덱스로 하는 값을 더해줌

