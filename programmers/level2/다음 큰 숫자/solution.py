'''
    Date : 2022년 10월 21일
    Author : 이푸름
    Description: 프로그래머스 다음 큰 숫자
'''

def findNext(nextN, cnt):
    nextCnt = 0
    while cnt != nextCnt:
        nextN += 1
        binary = format(nextN, 'b')
        nextCnt = binary.count('1')
    return nextN
    

def solution(n):
    binary = format(n, 'b')
    answer = findNext(n, binary.count('1'))
    return answer