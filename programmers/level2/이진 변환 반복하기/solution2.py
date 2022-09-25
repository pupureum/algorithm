'''
    Date : 2022년 9월 25일
    Author : 이푸름
    Description: 프로그래머스 이진 변환 반복하기 더 나은 버전
'''

def solution(s):
    cnt = 0
    num = 0
    while True:
        if s == '1':
            break
        num = num + s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
    answer = [cnt, num]
    return answer