N = int(input())

# [A, B, C, D, E, F]. A(0)-F(5) / B(1)-D(3) / C(2)-E(4)
data = [list(map(int, input().split())) for _ in range(N)]

opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

ans = 0
# 맨 밑 정해지면 그 위로는 자동으로 정해짐 => 맨 밑만 돌려가며 6가지 탐색
for i in range(len(data[0])):
    temp = 6 * N
    idx = 0
    bottom = data[idx][i]
    top = data[idx][opposite[i]]
    while idx < N:
        nxt_bottom_idx = data[idx].index(top)
        nxt_top_idx = opposite[nxt_bottom_idx]

        if data[idx][nxt_bottom_idx] + data[idx][nxt_top_idx] == 11:
            temp -= 2
        elif data[idx][nxt_bottom_idx] == 6 or data[idx][nxt_top_idx] == 6:
            temp -= 1

        top = data[idx][nxt_top_idx]
        idx += 1

    if temp > ans:
        ans = temp

print(ans)
