dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 각 cctv 별 이동 가능 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]],
}


def dfs(k, cnt):
    global max_val

    if k == cctv_cnt:  # 모든 cctv 탐색한 경우
        if max_val < cnt:
            max_val = cnt
        return

    cur_num, r, c = cctv[k]

    for ds in direction[cur_num]:  # 딕셔너리에서 이동 가능 방향 모음 하나씩 꺼냄
        temp = []  # total_map 초기화 위한 리스트
        cur_cnt = 0  # 현재 방향 모음에서 채운 공간 수
        for d in ds:  # 방향 모음에서 방향 하나씩 꺼내서 해당 방향으로 벽 만나거나 끝까지 #으로 채움
            cur_r, cur_c = r, c
            while True:
                nxt_r = cur_r + dr[d]
                nxt_c = cur_c + dc[d]
                if 0 <= nxt_r < N and 0 <= nxt_c < M:
                    if total_map[nxt_r][nxt_c] == 6:  # 벽 만난 경우
                        break
                    else:
                        if total_map[nxt_r][nxt_c] == 0:
                            total_map[nxt_r][nxt_c] = "#"
                            cur_cnt += 1
                            temp.append((nxt_r, nxt_c))
                        cur_r, cur_c = nxt_r, nxt_c
                else:  # 끝 도달한 경우
                    break
        dfs(k + 1, cnt + cur_cnt)

        for row, col in temp:  # 다음 방향 모음 탐색 위해 초기화
            total_map[row][col] = 0


N, M = map(int, input().split())  # N 세로 M 가로

total_map = []

wall = 0  # 벽의 개수
target = 0  # 빈 공간 개수
cctv = []
cctv_cnt = 0  # cctv 개수

for row in range(N):
    data = list(map(int, input().split()))
    total_map.append(data)
    for col in range(M):
        if data[col] == 6:
            wall += 1
        elif data[col] == 0:
            target += 1
        else:
            cctv.append((data[col], row, col))  # cctv종류, r, c
            cctv_cnt += 1

max_val = 0  # cctv로 감시할 수 있는 최대 공간

dfs(0, 0)

print(target - max_val)
