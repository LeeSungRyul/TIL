# 난이도 - 실버

## ✅ 1541. 잃어버린 괄호

### I. 첫 번째 풀이

```python
og = input()

new_str = og[0]
temp = []

for i in range(1, len(og)):
    if new_str[-1] == '-':
        new_str += '(' + og[i]
        temp.append('(')
        continue
    if og[i] == '-' and temp:
        new_str += ')' + og[i]
        temp.pop()
        continue
    new_str += og[i]
        

if temp:
    new_str += ')'

print(eval(new_str))
```

- 문제점

  `eval()` 사용하여 문자열을 계산할 경우, 숫자가 0으로 시작할 경우 계산할 없고 에러 발생

### II. 두 번째 풀이

```python
og = input()

ans = 0
minus_split = og.split('-')
for i in range(len(minus_split)):
    plus_split = list(map(int, minus_split[i].split('+')))
    if i == 0:
        ans += sum(plus_split)
    else:
        ans -= sum(plus_split)
print(ans)
```

- 핵심 - '-'를 기준으로 `split()`하고 다시 '+'를 기준으로 `split()`

# 난이도 - 골드

## ✅ 1339. 단어 수학

> N개의 단어를 입력받아, 각 알파벳을 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제

```python
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
```

- 핵심 - **10의 지수로 자리에 가중치 설정**

  처음에는 문자의 길이가 긴 것부터 해서 앞에서부터 딕셔너리에 넣으며 풀려했으나, 길이가 같아질 경우 처리하는 방법이 너무 복잡해짐

  따라서, 길이 순으로 정렬하지 않고도 해당 자리에 10의 지수로 가중치를 주어서 딕셔너리에 가중치 합을 value로 저장하면, 나중에 value를 오름차순으로 정렬하여 9부터 0까지 곱해서 더해주기만 하면 된다.