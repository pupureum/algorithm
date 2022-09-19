'''
    Date : 2022년 9월 19일
    Author : 이푸름
    Description: 프로그래머스 최솟값 만들기
'''

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer