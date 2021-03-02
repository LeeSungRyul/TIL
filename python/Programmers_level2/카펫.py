def solution(brown, yellow):
    answer = []
    li_y = []

    if yellow == 1:
        return [3, 3]
    else:
        for i in range(1, brown - 1):
            for j in range(1, i + 1):
                if i * j == yellow:
                    li_y.append([i, j])
        for i in li_y:
            if i[0] * 2 + i[1] * 2 + 4 == brown:
                answer = [i[0] + 2, i[1] + 2]
                break

    return answer

# 추천 풀이
'''
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
'''