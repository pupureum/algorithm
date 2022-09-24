'''
    Date : 2022년 9월 24일
    Author : 이푸름
    Description: 프로그래머스 숫자의 표현
'''

def isConsecutive(i, n):
    sum = 0
    for j in range(i, n + 1):
        if sum == n:
            return True
        if sum > n:
            return False
        sum += j
        
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i == n:
            answer += 1
            break
        if isConsecutive(i, n) == True:
            answer += 1
    return answer