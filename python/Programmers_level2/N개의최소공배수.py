def lcd(a, b):
    c, d = max(a, b), min(a, b)
    t = 1

    while (t > 0):
        t = c % d
        c, d = d, t
    return int((a * b) / c)

def solution(arr):
    arr.sort()

    for i in range(len(arr) - 1):
        arr[i + 1] = lcd(arr[i], arr[i + 1])

    return arr[-1]

# 추천 풀이
# from fractions import gcd
#
# def nlcm(num):
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)
#
#     return answer