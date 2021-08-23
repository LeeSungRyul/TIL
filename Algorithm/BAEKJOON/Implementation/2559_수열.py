N, K = map(int, input().split())

data = list(map(int, input().split()))
ans = sum(data[:K])
temp = ans
for i in range(K, N):
    temp = temp - data[i - K] + data[i]
    if ans < temp:
        ans = temp

print(ans)
