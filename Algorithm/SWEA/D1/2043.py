ans, now = map(int, input().split(' '))

cnt = 0

while True:
    cnt += 1
    if ans == now:
        break
    now += 1

    if now > 999:
        now = 0
print(cnt)