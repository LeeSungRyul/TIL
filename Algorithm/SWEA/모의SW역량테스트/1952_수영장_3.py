"""
DP
"""

from collections import deque


T = int(input())


for tc in range(1, T + 1):
    p_d, p_1, p_3, p_y = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    dp = [0] * 13

    dp[1] = min(p_1, data[1] * p_d)
    dp[2] = dp[1] + min(p_1, data[1] * p_d)

    for i in range(3, 13):
        dp[i] = min(dp[i - 3] + p_3, dp[i - 1] + p_1, dp[i - 1] + p_d * data[i])

    print("#{} {}".format(tc, min(dp[12], p_y)))
