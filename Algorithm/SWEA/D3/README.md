## ✅1215, 1216, 4861

```python
T = 10

def check_palindrome(data, N, M, row):
    for i in range(N - M + 1):
        result = True
        for j in range(M // 2):
            if data[row][i + j] != data[row][i + M - 1 - j]:
                result = False
                break
        else:  # 안쪽 for문이 다 돌면 True 반환
            return result
    # 바깥쪽 for문이 다 돌면 False 반환
    return result


for _ in range(T):
    N = 100
    tc = int(input())
    data = [tuple(input()) for _ in range(N)]
    data_reverse = list(zip(*data))  # 세로 방향 회문 체크할 전치행렬

    row = 0  # 체크할 row idx
    ans = 1  # 회문의 최소 길이는 1

    while row < N:  # row는 0~99 까지 모두 체크해야 최대 길이 확인 가능
        for M in range(N, 0, -1):  # M은 회문의 길이. 최대 회문 길이 찾는 것이므로 끝에서부터 탐색
            if M == ans:
                break
            if check_palindrome(data, N, M, row) or check_palindrome(
                data_reverse, N, M, row
            ):  # 하나라도 회문 가지면
                if ans < M:  # 현재 M이 ans보다 큰 경우, ans 변경
                    ans = M
                break  # 최대길이 회문 찾은 경우, 더이상 해당 idx 탐색 필요 X
        row += 1

    print("#{} {}".format(tc, ans))

```

- 회문 문제의 경우, 내가 한 풀이 중에서는 `.zip` 함수 활용하여 전치 행렬 통해 row로 한 번에 접근하고, 회문의 길이 M을 바꿔가며 M 범위 내에서 처음과 끝 글자를 비교해가며 하는 것이 속도가 가장 잘 나옴
