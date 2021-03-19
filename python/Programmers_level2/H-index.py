def solution(citations):
    answer = 0
    citations.sort()

    for i, v in enumerate(citations):
        if v >= len(citations) - i:
            answer = len(citations) - i
            break

    return answer