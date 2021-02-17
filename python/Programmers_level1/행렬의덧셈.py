def solution(arr1, arr2):
    line = len(arr1[1])
    row = len(arr1)
    answer = []

    for i in range(row):
        temp = []
        for j in range(line):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer

# 추천 풀이
# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer