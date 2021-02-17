def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

# 추천 풀이
# def solution(a, b):
#
#     return sum([x*y for x, y in zip(a,b)])    # zip 함수는 두 개의 리스트를 하나의 연관된 리스트로 만듦