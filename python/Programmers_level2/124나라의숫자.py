def solution(n):
    answer = 0
    remainder = []

    while n > 0:
        remainder.append(n % 3)
        n = n // 3

    for i in range(len(remainder)):
        if i != (len(remainder) - 1):
            if remainder[i] == 1 or remainder[i] == 2:
                answer += 10 ** i * remainder[i]
            elif remainder[i] == -1:
                remainder[i + 1] -= 1
                answer += 10 ** i * 2
            else:
                remainder[i + 1] -= 1
                answer += 10 ** i * 4
        else:
            if remainder[i] == 1 or remainder[i] == 2:
                answer += 10 ** i * remainder[i]
            elif remainder[i] == -1:
                answer += 10 ** i * 2

    return str(answer)

# 추천 풀이
'''
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
'''