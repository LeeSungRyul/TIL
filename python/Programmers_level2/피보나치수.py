def solution(n):  # 재귀함수로 풀면 재귀함수 깊이 초과
    li_n = [0, 1]

    if n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            # (A + B) % C = (A%C + B%C) % C
            li_n.append((li_n[i - 1] % 1234567 + li_n[i - 2] % 1234567) % 1234567)

    return li_n[n]

# 추천 풀이
# def fibonacci(num):
#     a,b = 0,1
#     for i in range(num):
#         a,b = b,a+b
#     return a