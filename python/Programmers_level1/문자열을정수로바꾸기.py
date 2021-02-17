def solution(s):
    answer = int(s)
    return answer

# 추천 풀이
# def strToInt(str):
#     result = 0
#
#     for idx, number in enumerate(str[::-1]):      # str[::]: 문자열 정방향  str[::-1]: 문자열 역방향
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10 ** idx)
#
#     return result