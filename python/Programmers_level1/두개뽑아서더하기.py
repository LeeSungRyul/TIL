def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.append(temp)

    answer.sort()

    return answer

# 추천 풀이
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))