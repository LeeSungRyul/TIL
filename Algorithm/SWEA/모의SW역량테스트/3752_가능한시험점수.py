import sys

sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    max_sum = sum(data)

    chk = [0 for _ in range(max_sum + 1)]

    chk[0] = 1  # 공집합

    for num in data:
        for i in range(max_sum, -1, -1):
            if chk[i]:
                chk[i + num] = 1

    ans = sum(chk)

    print("#{} {}".format(tc, ans))
