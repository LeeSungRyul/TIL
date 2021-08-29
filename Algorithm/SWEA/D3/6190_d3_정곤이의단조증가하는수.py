T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            target = data[i] * data[j]
            prev = target % 10
            temp = target // 10

            if not temp:
                if ans < target:
                    ans = target
                continue

            while temp > 0:
                cur = temp % 10
                temp //= 10

                if cur > prev:
                    break

                prev = cur

            else:
                if ans < target:
                    ans = target

    print("#{} {}".format(tc, ans))
