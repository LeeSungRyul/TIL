def solution(s):
    length = len(s)
    length_half = len(s) // 2

    if length % 2 == 1:
        answer = s[length_half]
    else:
        answer = s[length_half - 1] + s[length_half]

    return answer

# 추천 코드
# def string_middle(str):

#     return str[(len(str)-1)//2:len(str)//2+1]