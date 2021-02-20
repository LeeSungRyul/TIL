def solution(arr, divisor):
    answer = [n for n in arr if n % divisor == 0]
    answer.sort()
    if len(answer) == 0: answer.append(-1)

    return answer

# 추천 풀이
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
