def solution(bridge_length, weight, truck_weights):
    answer = 0
    out_bridge = []
    on_bridge = [0 for i in range(bridge_length)]
    bridge_weight = 0   # sum(on_bridge)로 하면 시간초과

    while (1):
        answer += 1

        if on_bridge[0] != 0:
            out_bridge.append(on_bridge[0])

        bridge_weight -= on_bridge[0]
        on_bridge.pop(0)

        if bridge_weight == 0 and len(truck_weights) == 0:
            break

        if len(truck_weights) != 0 and bridge_weight + truck_weights[0] <= weight:
            on_bridge.append(truck_weights[0])
            bridge_weight += truck_weights[0]
            truck_weights.pop(0)
        else:
            on_bridge.append(0)

    return answer

# 추천 풀이
'''

'''