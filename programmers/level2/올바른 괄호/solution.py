'''
    Date : 2022년 9월 20일
    Author : 이푸름
    Description: 프로그래머스 올바른 괄호
'''

def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[0] == ")" or (len(stack) == 0 and s[i] == ")"):
            return False
        if s[i] == "(":
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) != 0:
        answer = False
    return answer