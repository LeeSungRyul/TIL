T = 10

for tc in range(1, T + 1):
    N = int(input())
    # 1 N극 2 S극 윗부분 N극 아래부분 S극
    data = [list(map(int, input().split())) for _ in range(N)]
    data_reverse = list(zip(*data))

    ans = 0

    for row in data_reverse:
        stack = []
        for magnetic in row:
            if not magnetic:  # 0인 경우
                continue
            else:
                if not stack and magnetic == 1:
                    stack.append(magnetic)
                elif stack and magnetic == 2:
                    stack.pop()
                    ans += 1

    print("#{} {}".format(tc, ans))
