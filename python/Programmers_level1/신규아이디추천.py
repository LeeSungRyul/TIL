def solution(new_id):
    answer = ''
    valid_ch = ['-', '_', '.']
    remove = []

    # 소문자 치환
    temp = list(new_id.lower())
    # 다른 문자 제거
    for i in range(len(temp)):
        if not ('a' <= temp[i] <= 'z' or '0' <= temp[i] <= '9' or temp[i] in valid_ch):
            remove.append(temp[i])
    for i in remove:
        if i in temp:
            temp.remove(i)
    # 연속된 . 제거 -> 문자열 함수 중 replace로 제거 가능
    remove_dot = []
    temp_dot = []
    for i in range(1, len(temp)):
        if temp[i] == '.' and temp[i - 1] == '.':
            remove_dot.append(i)
    for i in range(len(temp)):
        if i not in remove_dot:
            temp_dot.append(temp[i])
    # 처음, 마지막 . 제거 -> 처음 제거하면서 빈 리스트 되면 에러.
    if temp_dot[0] == '.':
        del temp_dot[0]
    if (len(temp_dot) > 0):
        if temp_dot[-1] == '.':
            del temp_dot[-1]
    # 빈 문자열 a 대입
    if len(temp_dot) == 0:
        temp_dot.append('a')
    # 16자 이상 제거
    if len(temp_dot) >= 16:
        del temp_dot[15:]
        if temp_dot[14] == '.':
            temp_dot.pop(14)
    # 2자 이하
    if len(temp_dot) <= 2:
        while (len(temp_dot) < 3):
            temp_dot.append(temp_dot[len(temp_dot) - 1])
    # 답 출력
    for i in temp_dot:
        answer += i

    return answer

# 추천 풀이
# def solution(new_id):
#     answer = ''
    # 1
#     new_id = new_id.lower()
    # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
    # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
    # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
    # 5
#     if answer == '':
#         answer = 'a'
    # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
    # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer