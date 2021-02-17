def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        answer += i

    return answer

# 추천 풀이
# def adder(a, b):
#     if a > b: a, b = b, a

#    return sum(range(a,b+1)