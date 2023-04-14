from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        document = d.popleft()
        if d and max(d)[0] > document[0]:
            d.append(document)
        else:
            answer += 1
            if document[1] == location:
                break
    return answer    

print(solution([1, 1, 1, 2], 2))