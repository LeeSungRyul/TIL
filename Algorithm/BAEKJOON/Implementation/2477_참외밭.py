import sys

K = int(sys.stdin.readline())  # 1 m^2 당 참외 개수
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

cnt = [0 for _ in range(5)]

for command in commands:  # 각 방향 개수 계산
    cnt[command[0]] += 1

for i in range(len(commands)):  # 온전한 변부터 넣어주면 짧은 변들 계산할 때 2, 3번째 값만 가져오면 됨
    if cnt[commands[i][0]] == 1:  # 온전한 변 찾으면
        break
commands = commands[i:] + commands[:i]  # commands 순서 바꿔줌

temp = []  # 짧은 변들 넣어줄 리스트
for command in commands:
    if cnt[command[0]] == 1:  # 온전한 변인 경우
        if command[0] == 1 or command[0] == 2:  # 가로
            width = command[1]
        else:  # 세로
            heigth = command[1]
    elif cnt[command[0]] == 2:  # 짧은 변인 경우
        temp.append(command[1])

ans = (heigth * width - temp[1] * temp[2]) * K

print(ans)
