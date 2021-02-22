def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x + x * i)

    return answer

# 추천 풀이
# def number_generator(x, n):
#
#     return [i * x + x for i in range(n)]