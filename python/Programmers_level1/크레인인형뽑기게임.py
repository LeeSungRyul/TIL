def solution(board, moves):
    answer = 0
    k = -1
    basket = []
    # 인형 꺼내오기
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            else:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                k += 1
                break
        # basket 안 터뜨리기
        if len(basket) > 1:
            if basket[k] == basket[k - 1]:
                basket.pop(k)
                basket.pop(k - 1)
                k -= 2
                answer += 2

    return answer