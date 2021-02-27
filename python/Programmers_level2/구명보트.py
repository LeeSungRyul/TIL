def solution(people, limit):    # 효율성 count로 해결
    answer = 0
    people.sort()
    f_count = 0
    e_count = len(people) - 1

    while e_count >= f_count + 1:
        if people[e_count] + people[f_count] > limit:
            e_count -= 1
        else:
            f_count += 1
            e_count -= 1
        answer += 1
    if e_count == f_count:
        answer += 1

    return answer

# 추천 풀이
# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer