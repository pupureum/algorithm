from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    print = 0
    while(len(queue)):
        document = queue.popleft()
        if len(queue) != 0:
            first = max(queue)
        if document >= first:
            print += 1
            if location == 0:
                return print
            location -= 1
        else:
            queue.append(document)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
    return print

print(solution([1, 1, 1, 2], 2))