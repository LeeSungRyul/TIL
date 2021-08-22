first_num = int(input())
ans = [first_num]

for i in range(first_num, 0, -1):
    second_num = i
    temp = [first_num, second_num]

    while True:
        num = temp[-2] - temp[-1]

        if num < 0:
            break

        temp.append(num)

    if len(ans) < len(temp):
        ans = temp[:]

print(len(ans))
print(*ans)
