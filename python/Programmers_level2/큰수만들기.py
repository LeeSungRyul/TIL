def solution(number, k):
    answer = ''
    temp = [number[0]]

    for n in number[1:]:
        while len(temp) > 0 and temp[-1] < n and k > 0:
            k -= 1
            temp.pop()
        temp.append(n)
    if k != 0:
        temp = temp[:-k]

    return ''.join(temp)