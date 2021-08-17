"""
글자수_1.py에서 sort 쓰는 거 피하기 위해 딕셔너리 사용
"""

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = list(input())
    cnt = {}
    for target in str1:
        cnt[target] = 0

    ans = 0

    for char in str2:
        # try:
        #     cnt[char] += 1
        # except:
        #     continue
        if char in cnt:
            cnt[char] += 1

    print(cnt)
    ans = 0
    # ans = max(cnt.values())
    for val in cnt.values():
        if ans < val:
            ans = val

    print("#{} {}".format(tc, ans))
