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