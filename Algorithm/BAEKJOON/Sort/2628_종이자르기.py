w, h = map(int, input().split())
N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]

square = [[0, w, 0, h]]
cutted = []

for i in range(len(point)):
    # 세로로 자를 때
    if point[i][0] == 1:
        for j in range(len(square)):
            if square[j][0] < point[i][1] < square[j][1] and j not in cutted:
                square.append([square[j][0], point[i][1], square[j][2], square[j][3]])
                square.append([point[i][1], square[j][1], square[j][2], square[j][3]])
                cutted.append(j)

    # 가로로 자를 때
    else:
        for j in range(len(square)):
            if square[j][2] < point[i][1] < square[j][3] and j not in cutted:
                square.append([square[j][0], square[j][1], square[j][2], point[i][1]])
                square.append([square[j][0], square[j][1], point[i][1], square[j][3]])
                cutted.append(j)

ans = 0
for i in range(len(square)):
    if i not in cutted:
        temp = (square[i][1] - square[i][0]) * (square[i][3] - square[i][2])
        if temp > ans:
            ans = temp

print(ans)
