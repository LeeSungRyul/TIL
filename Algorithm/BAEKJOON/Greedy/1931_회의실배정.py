import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda time: (time[1], time[0]))

start = 0
end = 0
ans = 0

for d in data:
    if d[0] >= end:
        start = d[0]
        end = d[1]
        ans += 1

print(ans)