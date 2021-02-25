def solution(n, arr1, arr2):
    answer = []
    # OR 계산
    for i in range(n):
        answer.append(arr1[i] | arr2[i])
    answer = [bin(i) for i in answer]
    # #으로 전환
    for i in range(len(answer)):
        temp = answer[i].replace('1', '#')
        temp = temp.replace('0', ' ')
        answer[i] = temp
    answer = [i[2:] for i in answer]
    for i in range(len(answer)):
        while (len(answer[i]) != n):
            answer[i] = ' ' + answer[i]

    return answer

# 추천 풀이
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = bin(i|j)[2:]    # bin()의 return : str
#         a12=  a12.rjust(n,'0')    # rjust(문자열크기, 공백채울문자) : 오른쪽 정렬
#         a12 = a12.replace('1','#')
#         a12 = a12.replace('0',' ')
#         answer.append(a12)
#     return answer