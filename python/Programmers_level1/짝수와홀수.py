def solution(num):
    answer = ''

    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer

# 추천 풀이
# def evenOrOdd(num):
#     return ["Even", "Odd"][num & 1]   # 한 자리만 비트 연산