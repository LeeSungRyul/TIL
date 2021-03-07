def solution(clothes):
    answer = {}
    for i in clothes:   # 종류별로 갯수 세기
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)    # 종류별 갯수 + 안 입는 경우
    return cnt - 1  # 아무것도 안 입은 경우 빼기

# 추천 풀이
'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''