def solution(prices):
    from collections import deque
    answer = []
    dq = deque(prices)

    while len(dq):
        count = 0
        temp = dq.popleft() # list.pop(0)로 하면 시간 초과
        for i in dq:    # in range(len(dq))로 하면 시간 초과
            count += 1
            if i < temp:
                break
        answer.append(count)

    return answer

# 추천 풀이
'''
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
'''