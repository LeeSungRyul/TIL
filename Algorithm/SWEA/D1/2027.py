ans = []

for i in range(5):
    plus_lst = ['+'] * 5
    plus_lst[i] = '#'
    ans.append(''.join(plus_lst))

print('\n'.join(ans))