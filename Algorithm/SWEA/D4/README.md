## ✅1210

- 첫 접근 - 위에서부터 1인 지점 찾아서 아래로 내려가면서 끝이 2인지 확인

``` python
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    ans = 0
    # 위에서부터 하나씩 내려가면서 끝이 2인지 확인
    for i in range(N):
        x = i
        y = 0
        visited = [[0] * N for _ in range(N)]

        if ladder[y][x] == 1:
            while True:
                visited[y][x] = 1
                if x - 1 >= 0 and ladder[y][x - 1] == 1 and visited[y][x - 1] == 0:
                    x -= 1
                    continue
                elif x + 1 < N and ladder[y][x + 1] == 1 and visited[y][x + 1] == 0:
                    x += 1
                    continue
                else:
                    y += 1

                if y == 99:
                    break

            if ladder[y][x] == 2:
                ans = i
                break
        else:
            continue

    print("#{} {}".format(tc, ans))
```

- 두 번째 접근 - 끝에서 2인 곳 먼저 찾아 위에서 x 값만 가져옴

```python
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    ans = 0
    # 밑에서 2인 지점부터 시작하여 거꾸로 올라감
    x = ladder[99].index(2)
    y = 99
    visited = [[0] * N for _ in range(N)]

    while True:
        visited[y][x] += 1
        if x - 1 >= 0 and ladder[y][x - 1] == 1 and visited[y][x - 1] == 0:
            x -= 1
            continue
        elif x + 1 < N and ladder[y][x + 1] == 1 and visited[y][x + 1] == 0:
            x += 1
            continue
        else:
            y -= 1

        if y == 0:
            break
    ans = x

    print("#{} {}".format(tc, ans))
```

- 문제점
  - 조건을 맞게 썼다고 생각했는데 계속 Index Error가 발생
  - x - 1 > 0이나 x + 1 < N 같은 조건이 list 값 확인하기 전에 and 조건으로 먼저 있어야 Index Error 발생 막을 수 있다!!
- 배운점
  - 위에서부터 내려가면서 모든 값 확인하는 완전 탐색 같은 방법보다 밑에서 원하는 값 찾고 위로 올라오는게 반복 횟수를 훨씬 줄일 수 있다.
  - 방문 여부를 확인하기 위해 처음에 리스트에 넣고 `not in` 통해 찾았는데 그것보다 원본 데이터와 같은 크기의 2차원 배열 만들어서 인덱스로 접근하는 게 효율적
