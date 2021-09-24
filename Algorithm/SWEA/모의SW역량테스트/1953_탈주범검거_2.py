# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
connect = [2, 3, 0, 1]  # 연결된 정보

# 터널 구조물
pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],  # 상하좌우
    [0, 1, 0, 1],  # 상하
    [1, 0, 1, 0],  # 좌우
    [1, 0, 0, 1],  # 상우
    [1, 1, 0, 0],  # 하우
    [0, 1, 1, 0],  # 하좌
    [0, 0, 1, 1],  # 상좌
]

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1
        if visited[r][c] >= L:
            continue

        for d in range(4):
            cur_p = tunnel[r][c]

            if pipe[cur_p][d] == 0:
                continue

            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            nd = connect[d]
            np = tunnel[nr][nc]

            if visited[nr][nc] or pipe[nr][nc] == 0:
                continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))

    print("#{} {}".format(tc, ans))


##############################################################################

# 갈 수 있는 방향 저장
pipe = [
    [],
    [0, 1, 2, 3],  # 상하좌우
    [1, 3],  # 상하
    [0, 2],  # 좌우
    [0, 3],  # 상우
    [0, 1],  # 하우
    [1, 2],  # 하좌
    [2, 3],  # 상좌
]

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C, 1)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c, time = Q.pop(0)
        ans += 1
        if time >= L:
            continue

        for i in pipe[tunnel[r][c]]:
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if tunnel[nr][nc] == 0 or visited[nr][nc]:
                continue

            if (i + 2) % 4 in pipe[tunnel[nr][nc]]:
                Q.append((nr, nc, time + 1))
                visited[nr][nc] = 1

    print("#{} {}".format(tc, ans))
