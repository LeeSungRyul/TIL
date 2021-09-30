T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(cores, cnt, cnt_wire):
    global max_val, min_wire
    if not cores:
        if max_val < cnt:
            max_val = cnt
            min_wire = cnt_wire

        elif max_val == cnt:
            if min_wire > cnt_wire:
                min_wire = cnt_wire

        return

    if cnt + len(cores) < max_val:  # 최대 전원 연결 코어보다 현재 연결 코어 + 남은 코어 수 적은 경우 바로 종료
        return

    cur_row, cur_col = cores[0]
    start = (cur_row, cur_col)

    for d in range(4):  # 4방향 진행. 상하좌우 순
        temp = []  # visited 원상 복구
        temp_wire = 0  # wire 길이 원상 복구
        while True:
            nxt_row = cur_row + dr[d]
            nxt_col = cur_col + dc[d]
            if (
                nxt_row == 0
                or nxt_col == 0
                or nxt_row == N - 1
                or nxt_col == N - 1  # 전원 도착하면서 해당 지점 방문 X 경우
            ) and not visited[nxt_row][nxt_col]:
                visited[nxt_row][nxt_col] = 1
                temp.append((nxt_row, nxt_col))
                dfs(cores[1:], cnt + 1, cnt_wire + temp_wire + 1)
                break
            elif visited[nxt_row][nxt_col]:  # 해당 방향으로 진행 불가 경우 while 종료하고 초기화
                break
            else:  # 전원에 닿지는 않았으나 진행 가능한 경우
                visited[nxt_row][nxt_col] = 1
                temp.append((nxt_row, nxt_col))
                temp_wire += 1
                cur_row = nxt_row
                cur_col = nxt_col

        for i in range(len(temp)):
            visited[temp[i][0]][temp[i][1]] = 0
        cur_row = start[0]
        cur_col = start[1]

    dfs(cores[1:], cnt, cnt_wire)  # 해당 코어는 전원 연결 X


for tc in range(1, T + 1):
    N = int(input())

    visited = [[0] * N for _ in range(N)]
    cores = []  # 코어 위치
    cnt_core = 0  # 전체 코어 수

    for row in range(N):
        data = input().split()
        for col in range(N):
            if data[col] == "1":
                visited[row][col] = 2
                if row and col and row != N - 1 and col != N - 1:
                    cores.append((row, col))
                    cnt_core += 1

    max_val = 0
    min_wire = N * N + 1

    dfs(cores, 0, 0)
    print("#{} {}".format(tc, min_wire))
