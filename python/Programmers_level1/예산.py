def solution(d, budget):
    answer = 0
    d.sort()
    now = 0

    for i in d:
        if now + i > budget:
            break
        now += i
        answer += 1

    return answer

# 추천 풀이
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)