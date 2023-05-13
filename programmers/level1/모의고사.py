def solution(answers):
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1, score2, score3 = 0, 0, 0

    for i in range(len(answers)):
        i1 = i % 5
        i2 = i % 8
        i3 = i % 10
        if supoja1[i1] == answers[i]:
            score1 += 1
        if supoja2[i2] == answers[i]:
            score2 += 1
        if supoja3[i3] == answers[i]:
            score3 += 1
    
    answer = []
    max_score = max(score1, score2, score3)
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)  
    return answer

print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5]))