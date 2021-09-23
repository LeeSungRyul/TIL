from collections import deque
from copy import deepcopy
import sys

sys.stdin = open("input.txt")

T = int(input())


def find_start(data):
    starting = []
    height = -1

    for row in range(N):
        for col in range(N):
            if data[row][col] > height:
                height = data[row][col]
                starting = [(row, col)]
            elif data[row][col] == height:
                starting.append((row, col))

    return starting


def bfs(new_data, start):
    global ans
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < N:
                if new_data[nxt_row][nxt_col] < new_data[cur_row][cur_col]:
                    queue.append((nxt_row, nxt_col))
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                    if visited[nxt_row][nxt_col] > ans:
                        ans = visited[nxt_row][nxt_col]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    starting = find_start(data)
    for start in starting:
        bfs(data, start)

    for row in range(N):
        for col in range(N):
            for depth in range(1, K + 1):
                new_data = deepcopy(data)
                new_data[row][col] -= depth

                starting = find_start(new_data)

                for start in starting:
                    bfs(new_data, start)

    print("#{} {}".format(tc, ans))
