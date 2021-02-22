def solution(x):
    answer = True

    temp = list(map(int, str(x)))

    if x % sum(temp) != 0:
        answer = False

    return answer

# 추천 풀이
# def Harshad(n):
#
#     return n % sum([int(c) for c in str(n)]) == 0