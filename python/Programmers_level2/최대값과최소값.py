def solution(s):
    answer = ''
    temp = s.split(' ')
    temp = [int(i) for i in temp]   # line 3, 4 map 함수 사용하여 한 줄로 처리 가능
    temp_2 = [str(min(temp)), str(max(temp))]
    answer = ' '.join(temp_2)
    return answer

# 추천 풀이
# def solution(s):
#     s = list(map(int,s.split()))
#     return str(min(s)) + " " + str(max(s))