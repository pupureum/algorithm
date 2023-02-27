def checkAnswer(min_row, min_column, yellow):
    if (min_row - 2) * (min_column - 2) == yellow:
        return True
    return False

def calculate_pair(min_row, total):
    while(total % min_row != 0):
            min_row += 1
    print(min_row, total // min_row)
    return [min_row, total // min_row]

def solution(brown, yellow):
    min_row = 3 
    answer = calculate_pair(min_row, brown + yellow)
    while(True):
        if (checkAnswer(answer[0], answer[1], yellow)):
            break
        answer = calculate_pair(answer[0] + 1, brown + yellow)
    if answer[0] < answer[1]:
        return [answer[1], answer[0]]   
    return answer

print(solution(24,24))

# 공식을 정리해보면 다음과 같은 식을 얻을 수 있다.
# 2 * 가로 + 2 * 세로 = brown + 4 
# 이 식을 활용하면 더 깔끔한 코드로 가능
