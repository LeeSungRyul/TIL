input_str = input()

# 내장 함수 이용
# print(input_str.upper())

# ord('a') = 97 ord('z') = 122 ord('A') = 65
def to_upper(input_str):
    ans = ''
    for s in input_str:
        if 97 <= ord(s) <= 122:
            ans += chr(ord(s) - 32)
        else:
            ans += s
    return ans

print(to_upper(input_str))