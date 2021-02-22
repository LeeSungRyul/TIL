def solution(N, stages):
    answer = []
    fail_rate = []
    reach = 0
    fail = 0

    for i in range(1, N + 1):
        fail = stages.count(i)
        reach = len([x for x in stages if x >= i])
        if reach == 0:  # 아무도 도달하지 않은 경우. break 주면 그 뒤 스테이지 처리 X
            fail_rate.append([i, 0])
        else:
            fail_rate.append([i, fail / reach])

    fail_rate.sort(key=lambda fail_rate: fail_rate[1], reverse=True)

    answer = [fail_rate[i][0] for i in range(len(fail_rate))]

    return answer

# 추천 풀이
# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)