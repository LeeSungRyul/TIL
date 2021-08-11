T = int(input())

for tc in range(1, T + 1):
    # K: 한번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 타겟 정류장
    # M: 충전기 설치된 정류장 수
    K, N, M = map(int, input().split())
    gas_stations = tuple(map(int, input().split()))
    charged = K  # 현재 충전량
    ans = 0  # 충전 횟수
    gas_idx = 0  # 현재 위치하거나 다음에 위치한 주유소 idx

    for i in range(1, N + 1):  # 0에서 충전된 상태로 출발하므로 1부터 시작
        charged -= 1  # 한번 이동할 때마다 충전량 1 감소
        if gas_stations[gas_idx] == i:  # 현 위치가 gas station일 때
            if gas_idx == len(gas_stations) - 1:  # 마지막 gas station일 경우
                if K < N - i:  # 1회 충전 최대 거리가 남은 거리보다 짧은 경우
                    ans = 0
                    break
                elif charged >= N - i:  # 현재 충전량으로 다 갈 수 있는 경우
                    break
                elif K >= N - i:  # 현재 충전량으로는 부족하지만 다시 충전하면 갈 수 있는 경우
                    ans += 1
                    break
            else:  # 마지막 gas 스테이션 아닌 경우, 다음 충전소까지의 거리만 고려
                if charged < gas_stations[gas_idx + 1] - i:  # 이번 충전소에서 충전해야 하는 경우
                    charged = K  # 충전하고
                    ans += 1  # 충전 횟수 1 증가
                gas_idx += 1  # 주유소 지나가므로 idx 증가
        else:  # 현 위치가 gas station 아닐 때
            # 현재 충전량으로 남은 거리를 다 갈 수 없는 경우나 다음 주유소를 못 가는 경우는 이미 주유소인 경우에서 고려됨
            if charged == 0:  # 다음 충전소를 못 가거나 충전량 0이 된 경우
                ans = 0
                break

    print("#{} {}".format(tc, ans))
