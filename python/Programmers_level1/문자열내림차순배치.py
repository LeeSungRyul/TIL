def solution(s):
    answer = ''
    upper = []
    lower = []

    for i in s:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    lower.sort(reverse=True)    # reverse() 쓰면 역으로 배치만 하기 때문에 X
    upper.sort(reverse=True)

    for i in lower:
        answer += i
    for j in upper:
        answer += j

    return answer

# 추천 풀이
# def solution(s):
#     return ''.join(sorted(s, reverse=True))   # 문자열 정렬은 sorted. 아스키 코드 ord(). 'A' < 'a'
