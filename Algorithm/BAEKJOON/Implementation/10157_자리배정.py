C, R = map(int, input().split())
target = int(input())
cnt = 0
hall = [[0] * C for _ in range(R)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
d = 0
row = -1
col = 0

if target > C * R:
    print(0)
else:
    while True:
        nxt_row = row + dr[d]
        nxt_col = col + dc[d]
        if 0 <= nxt_row < R and 0 <= nxt_col < C and not hall[nxt_row][nxt_col]:
            cnt += 1
            hall[nxt_row][nxt_col] = cnt
            row = nxt_row
            col = nxt_col
            if cnt == target:
                print(col + 1, row + 1)
                break
        else:
            d = (d + 1) % 4
