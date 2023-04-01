import math

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        if i == 0:
            before = day
            count = 1
            continue
        if before >= day:
            count += 1
        else:
            answer.append(count)
            count = 1
            before = day
    answer.append(count)
    return answer