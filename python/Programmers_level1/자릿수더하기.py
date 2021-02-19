def solution(n):
    answer = 0

    str_n = str(n)

    for s in str_n:
        answer += int(s)

    return answer

# 재귀 함수
# def sum_digit(number):
#     if number < 10:
#         return number;
#     return (number % 10) + sum_digit(number // 10)

# sum 함수
# def sum_digit(number):
#     return sum([int(i) for i in str(number)])