import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda time: (time[1], time[0]))

start, end, ans = 0, 0 , 0

for d in data:
    if d[0] >= end:
        start, end = d[0], d[1] # start 변수는 굳이 없어도 됨
        ans += 1

print(ans)