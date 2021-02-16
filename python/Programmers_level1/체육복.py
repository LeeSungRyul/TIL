# 내 풀이
def solution(n, lost, reserve):
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    answer = n - len(lost)

    for k in lost:
        if reserve.count(k - 1):
            reserve.remove(k - 1)
            answer += 1
        elif reserve.count(k + 1):
            reserve.remove(k + 1)
            answer += 1

    return answer

# 가장 추천 많은 풀이

# def solution(n, lost, reserve):
#    _reserve = [r for r in reserve if r not in lost]
#    _lost = [l for l in lost if l not in reserve]
#    for r in _reserve:
#        f = r - 1
#        b = r + 1
#        if f in _lost:
#            _lost.remove(f)
#        elif b in _lost:
#            _lost.remove(b)
#    return n - len(_lost)
