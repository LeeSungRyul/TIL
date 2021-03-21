def solution(numbers):
    numbers = list(map(str, numbers))  # numbers list str로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True)  # labmda x: x*3 -> 해당 문자열 3번 반복

    return str(int(''.join(numbers)))

# 추천 풀이
'''
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
'''