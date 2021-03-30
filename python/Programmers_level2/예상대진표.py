def solution(n, a, b):  # math 써서 log. while True 조건 주고 하면 시간 초과
    answer = 0

    while a != b:
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return answer