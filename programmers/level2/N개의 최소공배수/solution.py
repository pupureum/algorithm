def solution(arr):
    arr.sort()
    answer = arr[-1]
    while(True):
        for i in range(len(arr) - 1):
            if (answer % arr[i] != 0):
                answer += arr[-1]
            if (i == len(arr) - 2):
                return answer
print(solution([2,6,8,14]))

# 개선한 코드!
# a와 b의 최소공배수를 x라고 하자, x = (a * b) / a, b의 최대공약수
from math import gcd

def advancedSolution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer * arr[i]) // gcd(answer, arr[i])
    return answer
