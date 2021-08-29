T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N 사람 수 M 초 K 개
    customers = list(map(int, input().split()))
    customers.sort()
    in_stock = [(i // M) * K for i in range(11112)]

    ans = "Possible"
    cnt = 0

    for customer in customers:
        cnt += 1

        if in_stock[customer] < cnt:
            ans = "Impossible"
            break

    print("#{} {}".format(tc, ans))
