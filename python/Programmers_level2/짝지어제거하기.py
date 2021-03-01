def solution(s):
    answer = 0
    temp = []

    if len(s) % 2 != 0:
        return 0
    else:
        for i in range(len(s)):
            temp.append(s[i])
            if len(temp) > 1 and temp[-1] == temp[-2]:
                temp.pop(-1)
                temp.pop(-1)
    if len(temp) == 0:
        answer = 1

    return answer

# 추천 풀이
'''
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)
'''