def solution(s):    # tile() 사용하면 숫자 제외하고 글자 대문자로 변경해서 오답
    answer = ''
    temp = list(s)
    li_answer = []

    for i in range(len(temp)):
        if temp[i] == ' ':
            li_answer.append(temp[i])
        else:
            if len(li_answer) == 0 or li_answer[-1] == ' ':
                li_answer.append(temp[i].upper())
            else:
                li_answer.append(temp[i].lower())
    answer = ''.join(li_answer)

    return answer