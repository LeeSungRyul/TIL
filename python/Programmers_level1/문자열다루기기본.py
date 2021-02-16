def solution(s):
    length = len(s)

    if length != 4 and length != 6:
        return False
    else:
        return s.isdigit()

# 추천 풀이
# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)