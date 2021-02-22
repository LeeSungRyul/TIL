def solution(n):
    temp = str(n)
    answer = []

    for i in range(len(temp)):
        answer.append(int(temp[i]))

    answer.reverse()

    return answer

# 추천 풀이 1. map 사용
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

# 추천 풀이 2
# def digit_reverse(n):
#     return [int(i) for i in str(n)][::-1]