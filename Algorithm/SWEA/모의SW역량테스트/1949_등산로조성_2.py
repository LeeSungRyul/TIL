"""
K 범위만큼 모두 탐색할 필요 없이 현재 높이보다 -1만큼 작을만큼만 깎음
1. 현재 높이를 들고 다니지 않을 때
2. 현재 높이를 들고 다닐 때
"""

from collections import deque
import sys

sys.stdin = open("input.txt")

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 현재 위치를 들고 다니지 않을 때
# r, c 좌표, road는 지금까지 조성된 등산로 길이, status는 공사 유무
def work(r, c, road, status):
    global ans

    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # a. 현 위치보다 낮은 곳으로 이동할 때
            if data[r][c] > data[nr][nc]:
                work(nr, nc, road + 1, status)
            # b. 현 위치보다 높거나 같은 곳으로 이동할 때
            elif status and data[r][c] > data[nr][nc] - K:
                temp = data[nr][nc]
                data[nr][nc] = data[r][c] - 1
                work(nr, nc, road + 1, 0)  # 공사 완료
                data[nr][nc] = temp  # 원상 복구

    visited[r][c] = 0


# 2. 현재 위치를 들고 다닐 때
def work2(r, c, h, road, status):
    global ans

    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]:
            continue
        if h > data[nr][nc]:
            work2(nr, nc, data[nr][nc], road + 1, status)
        elif status and h > data[nr][nc] - K:
            work2(nr, nc, data[r][c] - 1, road + 1, 0)

    visited[r][c] = 0


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    data = []
    starting = []
    max_h = 0

    for row in range(N):
        temp = list(map(int, input().split()))
        for col in range(N):
            if max_h < temp[col]:
                max_h = temp[col]
                starting = [(row, col)]
            elif temp[col] == max_h:
                starting.append((row, col))
        data.append(temp)

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for start in starting:
        work(start[0], start[1], 1, 1)
        # work2(start[0], start[1], max_h, 1, 1)

    print("#{} {}".format(tc, ans))
