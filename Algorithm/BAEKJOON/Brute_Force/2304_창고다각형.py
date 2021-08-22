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
