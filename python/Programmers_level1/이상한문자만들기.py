def solution(s):
    answer = ''
    temp = []

    temp = s.split(' ')

    for i, word in enumerate(temp):
        for j in range(len(word)):
            if j % 2 == 0:
                answer += word[j].upper()
            else:
                answer += word[j].lower()
        if not i == len(temp) - 1:
            answer += ' '

    return answer

# 비슷한 풀이. join 함수 사용
# def toWeirdCase(s):
#     res = []
#     for x in s.split(' '):
#         word = ''
#         for i in range(len(x)):
#             c = x[i].upper() if i % 2 == 0 else x[i].lower()
#             word = word + c
#         res.append(word)
#     return ' '.join(res)