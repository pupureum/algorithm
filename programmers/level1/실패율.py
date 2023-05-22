def solution(N, stages):
    answer = []
    stages.sort()
    length = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda data: -data[1])
    answer = [i[0] for i in answer]
    return answer