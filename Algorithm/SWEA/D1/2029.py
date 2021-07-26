T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(list(map(int, input().split())))

for i in range(len(case_lst)):
    print(f'#{i+1} {divmod(case_lst[i][0], case_lst[i][1])[0]} {divmod(case_lst[i][0], case_lst[i][1])[1]}')