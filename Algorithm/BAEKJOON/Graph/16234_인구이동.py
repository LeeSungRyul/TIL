# N x N, 인구수 차이 L 이상 R 이하일 때 이동
# Pypy3 로 했을 때는 통과, Python3로 했을 때는 80%에서 시간초과

N, L, R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]


def dfs(start):
    global cnt  # start 마다 누적시켜줘야 하므로 함수 바깥 변수 사용
    global total
    stack = [start]
    visited[start[0]][start[1]] = 1

    while stack:
        cur = stack.pop()
        cnt += 1  # 평균 구하기 위한 개수 계산
        total += data[cur[0]][cur[1]]  # 평균 구하기 위한 총합 계산
        cur_visited.append((cur[0], cur[1]))  # 현재 start에서 바꿔야하는 곳 저장하기 위한 리스트

        for i in range(4):  # 4 방향 확인하여 차이가 L 이상 R 이하인 방문하지 않은 곳이 있는지 확인
            nxt_row = cur[0] + dr[i]
            nxt_col = cur[1] + dc[i]
            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < N
                and L <= abs(data[cur[0]][cur[1]] - data[nxt_row][nxt_col]) <= R
                and not visited[nxt_row][nxt_col]
            ):
                stack.append((nxt_row, nxt_col))
                visited[nxt_row][nxt_col] = 1


dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

ans = 0

# while True:
while True:
    visited = [[0] * N for _ in range(N)]  # 2차원 리스트로 방문한 곳 판단. 도달할 수 있는 곳 평균으로 갱신하고 나면 visited 초기화
    # cnt가 1 이상이면 평균으로 변경시켜주는 곳이 있으므로, changed를 1로 바꿔주고, 1 이하이면 0으로 유지하면서 모든 칸 다 확인했는데
    # changed 0이면 while 문 종료
    changed = 0
    # 모든 칸 탐색
    for row in range(N):
        for col in range(N):
            if visited[row][col]:  # 이미 방문한 곳이면 pass
                continue
            cnt = 0
            total = 0
            cur_visited = []
            dfs((row, col))

            if cnt > 1:  # cur_visited가 2 이상이면, 해당 칸들 평균으로 변경
                for cur_visit in cur_visited:
                    data[cur_visit[0]][cur_visit[1]] = total // cnt
                changed = 1

    if not changed:
        break
    ans += 1

print(ans)
