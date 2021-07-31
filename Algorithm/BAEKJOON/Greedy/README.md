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