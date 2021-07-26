def calc_mean(lst):
    length = len(lst)
    total = sum(lst)
    return round(total / length)

T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(list(map(int, input().split(' '))))

for i in range(len(case_lst)):
    print(f'#{i+1} {calc_mean(case_lst[i])}')