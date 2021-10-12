"""
bfs 처리 과정에서 비활성화 바이러스인 곳과 빈 공간 구분 필요
"""

from collections import deque
from itertools import combinations

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(q):
    global ans
    cur_visited = [row[:] for row in visited]  # visited 복사해서 사용해서 bfs 탐색 후 초기화 과정 생략
    cnt = 0
    max_time = 0
    while q:
        cur_r, cur_c = q.popleft()

        for d in range(4):
            nxt_r = cur_r + dr[d]
            nxt_c = cur_c + dc[d]

            if 0 <= nxt_r < N and 0 <= nxt_c < N:
                if cur_visited[nxt_r][nxt_c] == -1:  # 빈 공간인 경우
                    cur_visited[nxt_r][nxt_c] = cur_visited[cur_r][cur_c] + 1  # visited 갱신
                    q.append((nxt_r, nxt_c))
                    cnt += 1  # 채워진 빈 공간 + 1
                elif cur_visited[nxt_r][nxt_c] == -2:  # 비활성 바이러스인 경우
                    cur_visited[nxt_r][nxt_c] = cur_visited[cur_r][cur_c] + 1  # visited 갱신
                    q.append((nxt_r, nxt_c))
                if cur_visited[nxt_r][nxt_c] > max_time:  # max_time 갱신
                    max_time = cur_visited[nxt_r][nxt_c]

        if cnt == target_cnt:  # 빈 공간 모두 채워진 경우
            break
    else:  # 빈 공간 모두 채우지 못한 경우
        return -1

    return max_time


N, M = map(int, input().split())  # N:연구소 크기  M: 초기 활성화 바이러스 개수

total_map = []  # 전체 연구소
walls = 0  # 벽의 개수
virus = []  # 초기 활성화/비활성화 바이러스 위치
virus_cnt = 0  # 초기 활성화/비활성화 바이러스 개수
visited = [[-1] * N for _ in range(N)]  # 빈 공간:-1  비활성화:-2  벽:-3  활성화:0

for row in range(N):
    data = list(map(int, input().split()))
    for col in range(N):
        if data[col] == 2:  # 초기 바이러스
            virus_cnt += 1
            virus.append((row, col))
            visited[row][col] = -2
        elif data[col] == 1:  # 벽
            visited[row][col] = -3
            walls += 1

target_cnt = N * N - walls - virus_cnt  # 빈 공간의 개수

if target_cnt == 0:  # 빈 공간 없는 경우
    print(0)
else:
    combis = combinations(virus, M)  # 활성화 바이러스 M개의 조합 만듦

    ans = -1
    for combi in combis:
        q = deque()
        for v in combi:  # 활성화 바이러스 위치 큐에 담고, 해당 visited는 0으로
            q.append(v)
            visited[v[0]][v[1]] = 0

        max_time = bfs(q)

        for v in combi:  # 다음 활성화 조합 탐색 위해 visited 초기화
            q.append(v)
            visited[v[0]][v[1]] = -2

        if ans == -1:  # ans = -1인 경우 무조건 max_time으로 갱신
            ans = max_time
        else:
            if max_time != -1 and ans > max_time:  # ans가 -1이 아닌 경우, max_time -1 아닌 때만 비교해서 갱신
                ans = max_time

    print(ans)
