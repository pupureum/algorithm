def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    # 앞에 모두 큰 숫자가 있는 경우 4321, 1도 있기에 슬라이싱 해준다.
    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("4321", 1))
