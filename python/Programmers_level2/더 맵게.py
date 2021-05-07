def solution(scoville, K):  # list, deque 쓰면 시간 초과. heapq는 항상 정렬된 상태
    import heapq

    heapq.heapify(scoville)
    answer = 0

    while True:
        answer += 1
        try:
            temp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            heapq.heappush(scoville, temp)
        except IndexError:  # pop 할 값 없는 경우 return -1
            return -1
        if scoville[0] >= K:
            break

    return answer

# 추천 풀이
'''
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''