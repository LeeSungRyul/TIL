## ✅ 2304. 창고 다각형

```python
N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: x[1])

max_idx, max_height = data.pop()
left_idx = max_idx
right_idx = max_idx

ans = max_height

while data:
    temp = data.pop()

    if temp[0] < left_idx:
        ans += (left_idx - temp[0]) * temp[1]
        left_idx = temp[0]
    elif temp[0] > right_idx:
        ans += (temp[0] - right_idx) * temp[1]
        right_idx = temp[0]

print(ans)
```

- 처음에 data에 기둥 좌표 및 높이 하나씩 넣고 data의 인덱스로 접근하려고 하니 같은 값일 때 처리해주기가 어려워짐
- 상준님 풀이 참고하여 해결
- 기둥 높이 기준으로 오름차순 정렬하여 가장 높은 기둥부터 좌우로 확인
