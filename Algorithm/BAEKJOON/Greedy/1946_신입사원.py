import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    data = []
    for _ in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))

    ans = 0
    data.sort(key=lambda score: score[0])
    previous_interview = N + 1

    for d in data:
        if d[1] < previous_interview:
            ans += 1
            previous_interview = d[1]

    print(ans)