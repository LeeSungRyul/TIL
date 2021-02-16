def solution(s):
    num_p = 0
    num_y = 0
    # 모두 소문자로, 그냥 lower만 쓰면 s 자체는 변경 X
    s = s.lower()
    # p 갯수
    num_p = s.count("p")
    # y 갯수
    num_y = s.count("y")
    # 비교
    if num_p == num_y:
        answer = True
    else:
        answer = False

    return answer

# 추천 풀이
# def numPY(s):

#     return s.lower().count('p') == s.lower().count('y')