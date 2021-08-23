def bingo_check(data):
    data_reverse = list(zip(*data))
    bingo_cnt = 0

    for row in range(5):
        row_cnt = 0
        reverse_cnt = 0
        for col in range(5):
            if data[row][col] == 0:
                row_cnt += 1
            else:
                break
        for col in range(5):
            if data_reverse[row][col] == 0:
                reverse_cnt += 1
            else:
                break
        if row_cnt == 5:
            bingo_cnt += 1
        if reverse_cnt == 5:
            bingo_cnt += 1

    diagonal_cnt = 0
    diagonal_reverse_cnt = 0
    for i in range(5):
        if data[i][i] == 0:
            diagonal_cnt += 1
        if data[i][4 - i] == 0:
            diagonal_reverse_cnt += 1

    if diagonal_cnt == 5:
        bingo_cnt += 1
    if diagonal_reverse_cnt == 5:
        bingo_cnt += 1

    return bingo_cnt


data = [list(map(int, input().split())) for _ in range(5)]
calls = []

for _ in range(5):
    calls += list(map(int, input().split()))

ans = 0

for i in range(len(calls)):
    for row in range(5):
        for col in range(5):
            if data[row][col] == calls[i]:
                data[row][col] = 0

            if i >= 11:  # 최소 경우는 12개 => 따라서 i는 11 이상
                bingo = bingo_check(data)
                if bingo >= 3:
                    ans = i + 1
                    break
        if ans:
            break
    if ans:
        break

print(ans)
