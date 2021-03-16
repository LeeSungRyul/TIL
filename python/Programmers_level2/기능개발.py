def solution(progresses, speeds):
    answer = []
    temp_list = []

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            temp_list.append((100 - progresses[i]) // speeds[i])
        else:
            temp_list.append((100 - progresses[i]) // speeds[i] + 1)

    while len(temp_list):
        count = 1
        temp = temp_list[0]
        temp_list.pop(0)

        while len(temp_list):
            if temp_list[0] > temp:
                break
            else:
                count += 1
                temp_list.pop(0)
        answer.append(count)

    return answer

# 추천 풀이
'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # ceil 없이 올림 쓰기 위함
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''