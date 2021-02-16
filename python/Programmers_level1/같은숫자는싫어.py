def solution(arr):
    answer = []

    for i in range(len(arr) - 1):           # len(arr)로 하면 arr[i+1]에서 범위 초과 에러
        if arr[i] != arr[i + 1]:            # 슬라이싱은 인덱스 범위 초과해도 에러나지 않음
            answer.append(arr[i])
    answer.append(arr[len(arr) - 1])

#   for i in range(len(arr)):               # 슬라이싱 이용
#       if [arr[i]] != arr[i + 1:i + 2]:    # [arr[i]]로 해서 list끼리 비교해야 함
#           answer.append(arr[i])
    
    return answer

# 추천 풀이
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue    # list a의 끝 값과 [i]를 비교하여 같으면 append X
#         a.append(i)
#     return a