N = int(input())
status = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, num = map(int, input().split())
    num -= 1

    if gender == 1:
        for i in range(num, N, num + 1):
            status[i] = 0 if status[i] else 1
    else:
        step = 0
        while num - step >= 0 and num + step < N:
            if status[num - step] != status[num + step]:
                break
            step += 1
        step -= 1  # while 조건에서 빠져나오거나 if 조건에 안 맞는 step이므로 1 빼줌

        for i in range(num - step, num + step + 1):
            status[i] = 0 if status[i] else 1
cnt = 0
for i in range(N):
    print(status[i], end=" ")
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0
