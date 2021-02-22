def solution(n):
    temp = list(map(int, str(n)))
    temp.sort(reverse=True)
    answer = ""

    for i in temp:
        answer += str(i)

    return int(answer)

# 추천 풀이
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))