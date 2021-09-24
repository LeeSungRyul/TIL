from collections import deque


T = int(input())


def calc(cost, m):
    global min_cost

    if m > 12:
        if cost < min_cost:
            min_cost = cost
        return

    # 1일권
    calc(cost + data[m] * p_d, m + 1)
    # 1달권
    calc(cost + p_1, m + 1)
    # 3달권
    calc(cost + p_3, m + 3)


for tc in range(1, T + 1):
    p_d, p_1, p_3, p_y = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    min_cost = p_y  # 1년치 비용이 초기 최저 가격

    calc(0, 1)

    print("#{} {}".format(tc, min_cost))
