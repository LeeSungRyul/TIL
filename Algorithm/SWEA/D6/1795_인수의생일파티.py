"""
다익스트라를 활용하는데
모든 노드에서 나가는 방향으로만 다익스트라 하면 시간 초과
타겟 노드에서 나가는 방향과 들어노는 방향으로 다익스트라 사용하면 해결
"""

import heapq
import sys

sys.stdin = open("input.txt")

T = int(input())
INF = 1000 * 100 + 1


def dijkstra_out(start):
    visited = [0] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist_out[start][v] = w

            for i in range(N + 1):
                if not visited[i]:
                    heapq.heappush(heap, (dist_out[start][v] + graph[v][i], i))


def dijkstra_in(start):
    visited = [0] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist_in[v][start] = w

            for i in range(N + 1):
                if not visited[i]:
                    heapq.heappush(heap, (dist_in[v][start] + graph[i][v], i))


for tc in range(1, T + 1):
    N, M, X = map(int, input().split())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    dist_out = [[INF] * (N + 1) for _ in range(N + 1)]
    dist_in = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x][y] = c

    dist_out[X][X] = 0
    dijkstra_out(X)
    dist_in[X][X] = 0
    dijkstra_in(X)

    ans = 0
    for i in range(1, N + 1):
        temp = dist_out[X][i] + dist_in[i][X]
        if ans < temp:
            ans = temp

    print("#{} {}".format(tc, ans))
