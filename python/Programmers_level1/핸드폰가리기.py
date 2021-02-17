def solution(phone_number):
    answer = ""

    for i in range(len(phone_number[:-4])):
        answer += "*"
    answer += phone_number[-4:]

    return answer

# 추천 풀이
#def hide_numbers(s):
#    return "*"*(len(s)-4) + s[-4:]