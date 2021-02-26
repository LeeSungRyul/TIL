def solution(numbers, hand):
    answer = ''
    pad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    now_l = pad[10]
    now_r = pad[11]

    for i in numbers:
        # 1, 4, 7
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            now_l = pad[i]
        # 3, 6, 9
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            now_r = pad[i]
        # 0, 2, 5, 8
        else:
            # 거리 계산. 거리를 유클리드(빼서 제곱)로 구하면 결과 다르게 나옴
            distance_l = abs(now_l[0] - pad[i][0]) + abs(now_l[1] - pad[i][1])
            distance_r = abs(now_r[0] - pad[i][0]) + abs(now_r[1] - pad[i][1])
            # 오른손 가까울 때
            if distance_l > distance_r:
                answer += 'R'
                now_r = pad[i]
            # 왼손 가까울 때
            elif distance_l < distance_r:
                answer += 'L'
                now_l = pad[i]
            # 거리 같을 때
            else:
                if hand == 'right':
                    answer += 'R'
                    now_r = pad[i]
                elif hand == 'left':
                    answer += 'L'
                    now_l = pad[i]

    return answer

# 추천 풀이. 딕셔너리 사용
# def solution(numbers, hand):
#     answer = ''
#     key_dict = {1:(0,0),2:(0,1),3:(0,2),
#                 4:(1,0),5:(1,1),6:(1,2),
#                 7:(2,0),8:(2,1),9:(2,2),
#                 '*':(3,0),0:(3,1),'#':(3,2)}
#
#     left = [1,4,7]
#     right = [3,6,9]
#     lhand = '*'
#     rhand = '#'
#     for i in numbers:
#         if i in left:
#             answer += 'L'
#             lhand = i
#         elif i in right:
#             answer += 'R'
#             rhand = i
#         else:
#             curPos = key_dict[i]
#             lPos = key_dict[lhand]
#             rPos = key_dict[rhand]
#             ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
#             rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
#
#             if ldist < rdist:
#                 answer += 'L'
#                 lhand = i
#             elif ldist > rdist:
#                 answer += 'R'
#                 rhand = i
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     lhand = i
#                 else:
#                     answer += 'R'
#                     rhand = i
#
#     return answer