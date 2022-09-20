'''
    Date : 2022년 9월 20일
    Author : 이푸름
    Description: 프로그래머스 올바른 괄호
'''

def solution(s):
    answer = True
    stack = []
    check = 0
    for i in range(len(s)):
        if s[0] == ")" or (len(stack) == 0 and s[i] == ")"):
            return False
        if s[i] == "(":
            check += 1
            stack.append(s[i])
        else:
            stack.pop()
            check -= 1
    if check > 0:
        answer = False
    return answer