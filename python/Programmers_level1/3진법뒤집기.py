def solution(n):
    answer_3 = []
    answer = 0

    while (n // 3 != 0):
        answer_3.append(n % 3)
        n = n // 3
    answer_3.append(n % 3)

    answer_3.reverse()

    for i, m in enumerate(answer_3):
        if m != 0:
            answer += m * (3 ** i)

    return answer

# 추천 풀이
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#
#     answer = int(tmp, 3)      # int(숫자or정수문자열, base)  ex> int('1a', 16) = 16 + 10 = 26
#     return answer