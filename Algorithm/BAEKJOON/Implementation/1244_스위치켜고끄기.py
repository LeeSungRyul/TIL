# 초기 스위치 상태를 입력받음
# 남학생의 경우, 입력 받은 숫자의 배수 스위치의 상태를 바꿔줌
# 여학생의 경우, 입력 받은 숫자를 기준으로 양 옆 숫자가 대칭인 곳까지 스위치 상태를 바꿔줌
N = int(input())
status = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, num = map(int, input().split())
    num -= 1  # 스위치 숫자는 1부터 시작하고 인덱스는 0부터 시작하므로 인덱스와 맞추기 위해 -1

    if gender == 1:  # 남학생의 경우
        for i in range(num, N, num + 1):  # 1을 빼준 num부터 시작하고, 간격은 1을 빼기 전 num이므로 1을 더해서 간격을 둔다.
            status[i] = 0 if status[i] else 1  # 스위치 상태를 바꿔주는 코드
    else:  # 여학생의 경우
        step = 0  # 양 옆을 체크하기 위한 step
        while (
            num - step >= 0 and num + step < N
        ):  # 입력받은 num에서 양 옆으로 step을 더하거나 빼준 값이 0보다 작거나 N보다 커지면 루프 빠져나옴
            if status[num - step] != status[num + step]:  # 양 옆 체크한 값이 다르면 루프 빠져나옴
                break
            step += 1  # 양 옆이 같은 경우, step을 늘려 더 넓은 범위 체크
        step -= 1  # 현재 step은 while 조건에서 빠져나오거나 if 조건에 안 맞는 step이므로 조건 만족하는 step을 가져오기 위해 1 빼줌

        for i in range(num - step, num + step + 1):
            status[i] = 0 if status[i] else 1
cnt = 0  # 한 줄에 20개를 세기 위한 변수
for i in range(N):
    print(status[i], end=" ")
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0
