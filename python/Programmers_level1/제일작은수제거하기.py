def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

# 추천 풀이
# def rm_small(mylist):
#     return [i for i in mylist if i > min(mylist)]