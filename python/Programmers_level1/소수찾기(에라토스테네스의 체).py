# 에라토스테네스의 체
def solution(n):
    answer = 0
    root_n = int(n ** 0.5)
    prime = [True] * (n + 1)

    for i in range(2, root_n + 1):
        if prime[i] == True:
            for j in range(i + i, n + 1, i):
                prime[j] = False

    prime_num = [i for i in range(2, n + 1) if prime[i] == True]

    answer = len(prime_num)

    return answer

# 추천 풀이
# def solution(n):
#     num=set(range(2,n+1))
#     root_n = int(n ** 0.5)
#
#     for i in range(2,root_n+1):
#         if i in num:
#             num -= set(range(i+i,n+1,i))  # 차집합 이용
#    return len(num)