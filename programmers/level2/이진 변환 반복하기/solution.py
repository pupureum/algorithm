'''
    Date : 2022년 9월 25일
    Author : 이푸름
    Description: 프로그래머스 이진 변환 반복하기
'''

def solution(s):
    cnt = 0
    num = 0
    newS = []
    while len(s) != 1:
        newS.clear()
        for i in range(len(s)):
            if s[i] == '0':
                num += 1
                continue
            else:
                newS += '1'
        s = bin(len(newS))[2:]
        cnt += 1
    answer = [cnt, num]
    return answer