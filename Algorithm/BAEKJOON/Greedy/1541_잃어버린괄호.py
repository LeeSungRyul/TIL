og = input()

# new_str = og[0]
# temp = []

# for i in range(1, len(og)):
#     if new_str[-1] == '-':
#         new_str += '(' + og[i]
#         temp.append('(')
#         continue
#     if og[i] == '-' and temp:
#         new_str += ')' + og[i]
#         temp.pop()
#         continue
#     new_str += og[i]
        

# if temp:
#     new_str += ')'

# print(eval(new_str))
ans = 0
minus_split = og.split('-')
for i in range(len(minus_split)):
    plus_split = list(map(int, minus_split[i].split('+')))
    if i == 0:
        ans += sum(plus_split)
    else:
        ans -= sum(plus_split)
print(ans)