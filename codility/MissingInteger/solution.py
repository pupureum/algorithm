'''
    Date : 2022년 9월 23일
    Author : 이푸름
    Description: 코딜리티 MissingInteger
'''

def solution(A):
    positive_set = set()
    for i in A:
        if i > 0:
            positive_set.add(i)
    positive = list(positive_set)
    positive.sort()
    answer = 1
    for i in positive:
        if answer < i:
            break
        else:
            answer += 1
    return answer