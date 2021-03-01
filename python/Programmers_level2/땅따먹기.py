def solution(land):
    answer = 0

    for i in range(len(land) - 1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    print(land[-1])
    answer = max(land[-1])

    return answer

# 추천 풀이
'''
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i -1][: j] + land[i - 1][j + 1:])

    return max(land[-1])
'''