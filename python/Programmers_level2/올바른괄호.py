def solution(s):
    answer = True
    temp = []

    for i in s:
        if i == '(':    # '(' temp에 넣기
            temp.append(i)
        else:   # ')'의 경우
            if len(temp) != 0 and temp[-1] == '(':  # 짝 맞은 '()' 제거
                temp.pop(-1)
            elif len(temp) != 0 and temp[-1] == ')':
                temp.append(i)
            else:   # 빈 temp에 ')' 넣는 경우
                answer = False
    if len(temp) != 0:  # temp 비어있지 않은 경우 False
        answer = False

    return answer

# replace 사용. 시간초과 효율성 에러
'''
def solution(s):        
    answer = True
    b_len = len(s)
    a_len = 0

    if b_len % 2 != 0:
        answer = False
    elif s.count('(') != b_len // 2:
        answer = False
    else:
        while (b_len != a_len):
            b_len = len(s)
            s = s.replace('()', '')
            a_len = len(s)
        if len(s) != 0:
            answer = False

    return answer
'''
# 추천 풀이
'''
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
'''