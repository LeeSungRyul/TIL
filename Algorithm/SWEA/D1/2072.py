def odd_sum(lst):
    total = 0
    for num in lst:
        if num%2:
            total += num
    return total

T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(list(map(int, input().split(' '))))

for i in range(len(case_lst)):
    print(f'#{i+1} {odd_sum(case_lst[i])}')