def solution(dartResult):
    answer = 0

    # 첫번째 숫자 계산
    num_1 = int(dartResult[0])
    dartResult = dartResult[1:]
    if num_1 == 1 and dartResult[0] == '0':
        num_1 = 10
        dartResult = dartResult[1:]

    if dartResult[0] == 'S':
        dartResult = dartResult[1:]
    elif dartResult[0] == 'D':
        num_1 = num_1 ** 2
        dartResult = dartResult[1:]
    elif dartResult[0] == 'T':
        num_1 = num_1 ** 3
        dartResult = dartResult[1:]

    if dartResult[0] == '*':
        num_1 = num_1 * 2
        answer += num_1
        dartResult = dartResult[1:]
    elif dartResult[0] == '#':
        num_1 = num_1 * (-1)
        answer += num_1
        dartResult = dartResult[1:]
    else:
        answer += num_1
    # 두번째 숫자 계산
    num_2 = int(dartResult[0])
    dartResult = dartResult[1:]
    if num_2 == 1 and dartResult[0] == '0':
        num_2 = 10
        dartResult = dartResult[1:]

    if dartResult[0] == 'S':
        dartResult = dartResult[1:]
    elif dartResult[0] == 'D':
        num_2 = num_2 ** 2
        dartResult = dartResult[1:]
    elif dartResult[0] == 'T':
        num_2 = num_2 ** 3
        dartResult = dartResult[1:]

    if dartResult[0] == '*':
        num_2 = num_2 * 2
        answer = answer + num_1 + num_2
        dartResult = dartResult[1:]
    elif dartResult[0] == '#':
        num_2 = num_2 * (-1)
        answer = answer + num_2
        dartResult = dartResult[1:]
    else:
        answer += num_2
    # 세번째 숫자 계산
    num_3 = int(dartResult[0])
    dartResult = dartResult[1:]

    if num_3 == 1 and dartResult[0] == '0':
        num_3 = 10
        dartResult = dartResult[1:]

    if dartResult[0] == 'D':
        num_3 = num_3 ** 2
    elif dartResult[0] == 'T':
        num_3 = num_3 ** 3

    if len(dartResult) > 1:
        dartResult = dartResult[1:]
        if dartResult[0] == '*':
            answer = answer + num_2 + num_3 * 2
        elif dartResult[0] == '#':
            answer = answer - num_3
    else:
        answer += num_3

    return answer

# 추천 풀이
# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#
#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)