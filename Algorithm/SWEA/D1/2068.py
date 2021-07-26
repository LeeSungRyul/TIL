T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(list(map(int, input().split(' '))))

for i in range(len(case_lst)):
    print(f'#{i+1} {max(case_lst[i])}')