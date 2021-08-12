import numpy as np
from itertools import chain

N = 100
area = [[0] * N for _ in range(N)]

T = 4

for _ in range(4):
    x_start, y_start, x_end, y_end = map(int, input().split())
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if area[y][x] == 0:
                area[y][x] += 1
# ans = sum(sum(area, []))  # sum 함수 이용해서 2차원 list -> 1차원 list
# ans = sum(list(chain(*area)))   # itertools.chain + unpacking 사용
ans = sum(np.array(area).flatten().tolist())  # numpy flatten 사용
print(ans)
