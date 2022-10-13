'''
    Date : 2022년 10월 13일
    Author : 이푸름
    Description: 프로그래머스 피보나치 수
'''

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

def solution(n): 
    fiboList = [0, 1]
    
    for i in range(n-1):
        fiboList.append(fiboList[i] + fiboList[i+1])
        
    return fiboList[n] % 1234567
