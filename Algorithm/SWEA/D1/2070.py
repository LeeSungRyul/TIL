def compare(lst):
    if lst[0] > lst[1]:
        return '>'
    elif lst[0] == lst[1]:
        return '='
    else:
        return '<'

T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(list(map(int, input().split(' '))))

for i in range(len(case_lst)):
    print(f'#{i+1} {compare(case_lst[i])}')