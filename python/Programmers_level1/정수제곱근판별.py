def solution(n):
    answer = 0

    if (n ** 0.5) % 1 == 0:
        answer = (int(n ** 0.5) + 1) ** 2
        return answer
    else:
        return -1