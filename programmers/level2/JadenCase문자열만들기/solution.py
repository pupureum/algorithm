'''
    Date : 2022년 9월 18일
    Author : 이푸름
    Description: 프로그래머스 JadenCase 문자열 만들기
'''

def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] == '':
            answer += ' '
        else:
            if not s[i][0].isdecimal():
                answer += s[i][0].upper() + s[i][1:].lower()
            else:
                answer += s[i][0] + s[i][1:].lower()
            answer += ' '
    return answer[:-1]

# 더 간단한 풀이
def betterSolution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return (' '.join(arr))