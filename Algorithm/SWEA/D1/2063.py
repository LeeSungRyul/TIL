def calc_median(lst):
    lst.sort()
    center_idx = len(lst) // 2
    return lst[center_idx]

# 9 <= N <= 199
# N은 항상 홀수
N = int(input())
input_lst = list(map(int, input().split(' ')))

print(calc_median(input_lst))