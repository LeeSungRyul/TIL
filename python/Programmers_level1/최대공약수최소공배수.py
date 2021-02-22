def solution(n, m):
    answer = []

    divisor_n = []
    divisor_m = []
    divisor_com = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisor_n.append(i)
    for j in range(1, m + 1):
        if m % j == 0:
            divisor_m.append(j)

    divisor_com = [i for i in divisor_n if i in divisor_m]
    answer = [max(divisor_com), max(divisor_com) * (n // max(divisor_com)) * (m // max(divisor_com))]

    return answer

# 추천 풀이. 유클리드 호제법
# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]
#
#     return answer
