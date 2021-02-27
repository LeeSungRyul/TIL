def solution(n):
    answer = 1  # 자기 자신
    num = 0
    i = 1
    li_n = [i for i in range(1, n + 1)]

    for i in range(n // 2):
        for j in range(i + 1, n // 2 + 2):
            if sum(li_n[i:j]) == n:
                answer += 1
                break
            elif sum(li_n[i:j]) > n:
                break

    return answer

# 추천 풀이
# def expressions(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])
# a+(a+1)+...+(a+k-1) = (k*(2a+k-1))/2 = n  ->  a = n/k + (1-k)/2
# 따라서, k는 n의 약수이면서 홀수인 갯수. 다만, k=2의 경우 a = (n-1)/2이므로 n이 홀수인 경우의 수 하나 추가
# 그러므로 n이 짝수라면 약수이면서 홀수인 갯수에 포함 안 되지만, 홀수는 포함되므로 n+1로 조건 부여