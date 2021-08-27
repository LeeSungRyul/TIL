import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

p += t
q += t
p %= 2 * w
q %= 2 * h

if p > w:
    p = w - (p - w)
if q > h:
    q = h - (q - h)

print(p, q)

# if p > w:
#     p = p - abs(p - w)
# if q > h:
#     w = w - abs(w - h)

# dx = [1, -1, 1, -1]
# dy = [1, 1, -1, -1]
# d = 0  # 초기 방향 오른쪽 위 대각선

# while t > 0:
#     p += dx[d]
#     q += dy[d]

#     if p == 0:  # 왼쪽 벽
#         if q == 0:  # 왼쪽 하단 모서리
#             d = 0
#         elif q == h:  # 왼쪽 상단 모서리
#             d = 2
#         else:  # 그 밖
#             d -= 1
#     elif p == w:  # 오른쪽 벽
#         if q == 0:  # 오른쪽 하단 모서리
#             d = 1
#         elif q == h:  # 오른쪽 상단 모서리
#             d = 3
#         else:  # 그 밖
#             d += 1
#     elif q == 0:  # 아래쪽 벽 (모서리는 위에서 판단)
#         d -= 2
#     elif q == h:  # 위쪽 벽 (모서리는 위에서 판단)
#         d += 2

#     t -= 1
