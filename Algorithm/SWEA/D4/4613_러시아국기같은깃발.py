T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    ans = N * M

    for w_r in range(N - 2):
        for b_r in range(w_r + 1, N - 1):
            temp = 0
            for row in range(0, w_r + 1):
                for col in range(M):
                    if data[row][col] != "W":
                        temp += 1

            for row in range(w_r + 1, b_r + 1):
                for col in range(M):
                    if data[row][col] != "B":
                        temp += 1

            for row in range(b_r + 1, N):
                for col in range(M):
                    if data[row][col] != "R":
                        temp += 1

            if ans > temp:
                ans = temp

    print("#{} {}".format(tc, ans))
