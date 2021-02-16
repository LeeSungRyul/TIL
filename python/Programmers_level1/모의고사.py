def solution(answers):
    answer = []
    score = []
    count_1 = 0
    count_2 = 0
    count_3 = 0
    sheet_1 = [1, 2, 3, 4, 5]
    sheet_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sheet_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == sheet_1[i % 5]:
            count_1 += 1
        if answers[i] == sheet_2[i % 8]:
            count_2 += 1
        if answers[i] == sheet_3[i % 10]:
            count_3 += 1

    score = [count_1, count_2, count_3]

    # enumerate(): 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포함하는 enumerate 객체 리턴
    for i, count in enumerate(score):
        if count == max(score):
            answer.append(i + 1)

    return answer