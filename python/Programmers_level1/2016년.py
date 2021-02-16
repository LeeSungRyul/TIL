def solution(a, b):
    answer = ''
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    count = 0

    if a > 1:
        for i in range(a - 1):
            count += month[i]

    count += b

    answer = week[count % 7]

    return answer

# 추천 코드
# def getDayName(a,b):
#     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     return days[(sum(months[:a-1])+b-1)%7]