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

## ✅5432

- 첫 시도

```python
T = int(input())

for tc in range(1, T + 1):
    data = input()

    pair = []
    raser = []
    stick_start = []
    stick_end = []
    # 첫 시도 제한시간 초과 => 시작, 끝, 레이저 리스트 순회하면서 데이터 커지면 시간 초과
    for i in range(len(data)):
        # 레이저 위치 append
        if i > 0 and data[i] == ")" and data[i - 1] == "(":
            raser.append(i - 1)
        # ( 는 pair에 넣고, 바로 다음이 )면 레이저, 아니면 막대 시작점
        if data[i] == "(":
            pair.append(data[i])
            if data[i + 1] != ")":
                stick_start.append(i)

        # 괄호 짝 맞으면 ( 하나 빼내줌
        if data[i] == ")" and pair[-1] == "(":
            pair.pop()
            # 바로 전이 ( 가 아니면 막대 끝점
            if i > 0 and data[i - 1] != "(":
                stick_end.append(i)

    ans = len(stick_start)
    for i in range(len(stick_start)):
        for r in raser:
            # 레이저가 막대 범위 안이면 잘리면서 개수 1개씩 증가
            if stick_start[i] < r < stick_end[i]:
                ans += 1
            # 레이저가 막대 끝보다 커지면 내부 반복 종료
            elif r > stick_end[i]:
                break

    print("#{} {}".format(tc, ans))
```

막대 시작점과 끝 점을 구하면서 레이저 위치 인덱스를 구해서, 그 후 시작점 갯수에 시작점과 끝점 사이에 포함되는 레이저 갯수를 더해주면서 답을 구함.

데이터 크기가 작은 경우에는 답이 나오나, 최대 길이가 100,000이어서 for문 한 번 내에 답을 구하고 싶었으나, 적절한 방법을 생각해내지 못 함.

- 해답 풀이

```python
T = int(input())

for tc in range(1, T + 1):
    data = input()

    pair = []
    ans = 0

    # data 최대 길이가 10만이므로 반복문 한바퀴 내에 끝내야 한다.
    for i in range(len(data)):
        # ( 는 pair에 넣음
        if data[i] == "(":
            pair.append(data[i])
        # 레이저의 경우, 짝 맞는 ( 하나 빼주고, 나머지 (는 레이저에 의해 잘리면서 그 갯수만큼 +1씩 된다
        elif i > 0 and data[i] == ")" and data[i - 1] == "(":
            pair.pop()
            ans += len(pair)
        # 막대의 끝인 경우, 잘리고 남은 부분인 하나만큼만 더해주면 된다
        else:
            pair.pop()
            ans += 1

    print("#{} {}".format(tc, ans))
```

핵심은 ')'의 경우 갯수를 세어주는 방법!

바로 붙어있는 () 레이저를 제외하고 pair 안에 있는 '('는 레이저에 의해 잘리는 막대이므로 그 갯수를 모두 더하고,

레이저가 아닌  ')'는 각 막대의 끝이므로, 잘리고 남은 1개씩 더해주면 된다.
