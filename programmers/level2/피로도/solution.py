from itertools import permutations

def solution(k, dungeons):
    answer = 0
    unit = []
    unit += list(permutations(dungeons, len(dungeons)))
    for i in range(len(unit)):
        stemina = k
        count = 0
        for u in unit[i]:
            if stemina < u[0]:
                break
            stemina -= u[1]
            count += 1
        answer = max(answer, count)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))