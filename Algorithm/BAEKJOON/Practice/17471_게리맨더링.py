from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline


def bfs(start, points):
    queue = deque()
    queue.append(start)
    visited[start] += 1
    ans = nums[start]
    cnt = 1

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if not visited[nxt] and nxt in points:
                visited[nxt] += 1
                cnt += 1
                ans += nums[nxt]
                queue.append(nxt)

    return cnt, ans


N = int(input())
nums = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        graph[i].append(temp[j + 1])


ans = -1
for i in range(1, N // 2 + 1):
    combis = combinations(range(1, N + 1), i)

    for combi in combis:
        points_1 = list(combi)
        points_2 = []
        for i in range(1, N + 1):
            if i not in points_1:
                points_2.append(i)
        visited = [0] * (N + 1)
        cnt1, ans1 = bfs(points_1[0], points_1)
        cnt2, ans2 = bfs(points_2[0], points_2)

        if cnt1 + cnt2 == N:
            if ans == -1 or ans > abs(ans1 - ans2):
                ans = abs(ans1 - ans2)

print(ans)
