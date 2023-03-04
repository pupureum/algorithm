import math

def solution(n):
    answer = 0
    for evenNum in range(n // 2 + 1):
        oddNum = n - evenNum * 2
        answer += math.factorial(oddNum + evenNum) // (math.factorial(oddNum) * math.factorial(evenNum))
    return answer % 1234567

print(solution(4))

# 로직
# 2칸 최대로 뛸 수 있는 개수 n을 구하기
# 2칸 개수 1개 줄이고 1칸 개수 2개 늘리기
# 2칸, 1칸의 총 개수! // 1칸 수의 개수! * 2칸 수의 개수!