def solution(s, n):
    answer = ''

    for x in s:
        if 'a' <= x <= 'z':
            if ord(x) + n > ord('z'):
                answer += chr(ord(x) + n - (ord('z') - ord('a') + 1))
            else:
                answer += chr(ord(x) + n)
        elif 'A' <= x <= 'Z':
            if ord(x) + n > ord('Z'):
                answer += chr(ord(x) + n - (ord('Z') - ord('A') + 1))
            else:
                answer += chr(ord(x) + n)
        else:
            answer += ' '

    return answer

# 추천 풀이
# def caesar(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
#
#     return "".join(s)