N = int(input())

test_case = []

for tc in range(N):
    word = input()
    test_case.append(word)

char_val = dict()
cur_max = 9

for word in test_case:
    weight = len(word) - 1
    for char in word:
        if char_val.get(char):
            char_val[char] += 10 ** weight
        else:
            char_val[char] = 10 ** weight
        weight -= 1

char_num = sorted(list(char_val.values()), reverse=True)
ans = 0
for num in char_num:
    ans += num * cur_max
    cur_max -= 1

print(ans)