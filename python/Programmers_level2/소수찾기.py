def sosu(number):
    num = set(range(2, number + 1))
    root_n = int(number ** 0.5)

    for i in range(2, root_n + 1):
        if i in num:
            num -= set(range(i + i, number + 1, i))
    return list(num)

def solution(numbers):
    answer = 0
    li_num = list(map(str, numbers))
    li_num.sort(reverse=True)
    max_num = int(''.join(li_num))
    li_sosu = list(map(str, sosu(max_num)))

    for i in li_sosu:
        for j in range(len(i)):
            if i.count(i[j]) > li_num.count(i[j]):
                break
            else:
                if j == len(i) - 1:
                    answer += 1

    return answer
# 추천 풀이. from itertools import permutations
'''
from itertools import permutations(순열. 순서고려)  # permutations(리스트, 조합갯수) return [(a,b),(a,c)] 형태
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))  # |= : OR 연산하여 대입
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

# 추가
from itertools import combinations(조합. 순서고려 X)
'''