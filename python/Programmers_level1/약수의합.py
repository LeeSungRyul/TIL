def solution(n):
    answer = 0
    divisor = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)
    answer = sum(divisor)

    return answer

# 추천 풀이
# def sumDivisor(num):
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
#     num / 2 의 수들만 검사하면 성능 약 2배 향상