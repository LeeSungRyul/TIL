def solution(s):
    answer = []
    count_bin = 0
    del_0 = 0
    temp = 0

    while (len(s) > 1):
        del_0 += s.count('0')
        s = s.replace('0', '')
        temp = len(s)
        s = bin(temp)[2:]
        count_bin += 1

    answer = [count_bin, del_0]

    return answer

# 추천 풀이
'''
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
'''