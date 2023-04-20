# 다음 인덱스에 해당하는 숫자 원소들을 더하거나 뺀 값을 방문하므로 dfs or bfs 모두 가능
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0, 0])
    while queue:
        sum, idx = queue.popleft()
        if idx == len(numbers):
            if sum == target:
                answer += 1
        else:
            queue.append([sum + numbers[idx], idx + 1])
            queue.append([sum - numbers[idx], idx + 1])
    return answer